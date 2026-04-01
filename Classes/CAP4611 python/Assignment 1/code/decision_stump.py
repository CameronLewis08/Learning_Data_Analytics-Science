import numpy as np
import utils


class DecisionStumpEquality:
    """
    This is a decision stump that branches on whether the value of X is
    "almost equal to" some threshold.

    This probably isn't a thing you want to actually do, it's just an example.
    """

    y_hat_yes = None
    y_hat_no = None
    j_best = None
    t_best = None

    def fit(self, X, y):
        n, d = X.shape

        # Get an array with the number of 0's, number of 1's, etc.
        count = np.bincount(y)

        # Get the index of the largest value in count.
        # Thus, y_mode is the mode (most popular value) of y
        y_mode = np.argmax(count)

        self.y_hat_yes = y_mode
        self.y_hat_no = None
        self.j_best = None
        self.t_best = None

        # If all the labels are the same, no need to split further
        if np.unique(y).size <= 1:
            return

        minError = np.sum(y != y_mode)
        # Loop over features looking for the best split
        for j in range(d):
            for i in range(n):
                # Choose value to equate to
                t = np.round(X[i, j])


                is_almost_equal = np.round(X[:, j]) == t
                y_yes_mode = utils.mode(y[is_almost_equal])
                y_no_mode = utils.mode(y[~is_almost_equal])  # ~ is "logical not"

                # Make predictions
                y_pred = y_yes_mode * np.ones(n)
                y_pred[np.round(X[:, j]) != t] = y_no_mode

                # Compute error
                errors = np.sum(y_pred != y)

                # Compare to minimum error so far
                if errors < minError:
                    # This is the lowest error, store this value
                    minError = errors
                    self.j_best = j
                    self.t_best = t
                    self.y_hat_yes = y_yes_mode
                    self.y_hat_no = y_no_mode

    def predict(self, X):
        n, d = X.shape
        X = np.round(X)

        if self.j_best is None:
            return self.y_hat_yes * np.ones(n)

        y_hat = np.zeros(n)

        for i in range(n):
            if X[i, self.j_best] == self.t_best:
                y_hat[i] = self.y_hat_yes
            else:
                y_hat[i] = self.y_hat_no

        return y_hat


class DecisionStumpErrorRate:
    y_hat_yes = None
    y_hat_no = None
    j_best = None
    t_best = None

    def fit(self, X, y):
        n, d = X.shape

        # Get an array with the number of 0's, number of 1's, etc.
        count = np.bincount(y)

        # Get the index of the largest value in count.
        # Thus, y_mode is the mode (most popular value) of y
        y_mode = np.argmax(count)

        self.y_hat_yes = y_mode
        self.y_hat_no = None
        self.j_best = None
        self.t_best = None

        # If all the labels are the same, no need to split further
        if np.unique(y).size <= 1:
            return

        minError = np.sum(y != y_mode)
        # Loop over features looking for the best split
        for j in range(d):
            for i in range(n):
                # Choose value to equate to
                t = np.round(X[i, j])


                is_almost_equal = (X[:, j] >= t - 3) & (X[:, j] <= t + 3)
                y_yes_mode = utils.mode(y[is_almost_equal])
                y_no_mode = utils.mode(y[~is_almost_equal])  # ~ is "logical not"

                # Make predictions
                y_pred = y_yes_mode * np.ones(n)
                y_pred[~is_almost_equal] = y_no_mode

                # Compute error
                errors = np.sum(y_pred != y)

                # Compare to minimum error so far
                if errors < minError:
                    # This is the lowest error, store this value
                    minError = errors
                    self.j_best = j
                    self.t_best = t
                    self.y_hat_yes = y_yes_mode
                    self.y_hat_no = y_no_mode

    def predict(self, X):
        n, d = X.shape
        X = np.round(X)

        if self.j_best is None:
            return self.y_hat_yes * np.ones(n)

        y_hat = np.zeros(n)

        for i in range(n):
            if self.t_best - 3 <= X[i, self.j_best] <= self.t_best + 3:
                y_hat[i] = self.y_hat_yes
            else:
                y_hat[i] = self.y_hat_no

        return y_hat

def entropy(p):
    """
    A helper function that computes the entropy of the
    discrete distribution p (stored in a 1D numpy array).
    The elements of p should add up to 1.
    This function ensures lim p-->0 of p log(p) = 0
    which is mathematically true, but numerically results in NaN
    because log(0) returns -Inf.
    """
    plogp = 0 * p  # initialize full of zeros
    plogp[p > 0] = p[p > 0] * np.log(p[p > 0])  # only do the computation when p>0
    return -np.sum(plogp)


class DecisionStumpInfoGain(DecisionStumpErrorRate):
    # This is not required, but one way to simplify the code is
    # to have this class inherit from DecisionStumpErrorRate.
    # Which methods (init, fit, predict) do you need to overwrite?
    y_hat_yes = None
    y_hat_no = None
    j_best = None
    t_best = None

    """YOUR CODE HERE FOR Q6.3"""

    def fit(self, X, y):
        n, d = X.shape
        n_classes = len(np.unique(y))

        # Calculate total entropy
        counts = np.bincount(y, minlength=n_classes)
        total_entropy = entropy(counts / counts.sum())

        max_info_gain = -1
        self.y_hat_yes = None
        self.y_hat_no = None
        self.j_best = None
        self.t_best = None

        # Try all features and thresholds
        for j in range(d):
            feature = X[:, j]
            # Use unique values as potential thresholds
            thresholds = np.unique(feature)

            for t in thresholds:
                # Standard decision stump split: >= threshold vs < threshold
                yes_mask = feature >= t
                no_mask = ~yes_mask

                y_yes = y[yes_mask]
                y_no = y[no_mask]

                # Skip if one side is empty
                if len(y_yes) == 0 or len(y_no) == 0:
                    continue

                # Calculate entropy for each split
                counts_yes = np.bincount(y_yes, minlength=n_classes)
                counts_no = np.bincount(y_no, minlength=n_classes)

                h_yes = entropy(counts_yes / counts_yes.sum())
                h_no = entropy(counts_no / counts_no.sum())

                # Calculate weighted average entropy
                weighted_entropy = (len(y_yes) * h_yes + len(y_no) * h_no) / n

                # Calculate information gain
                info_gain = total_entropy - weighted_entropy

                # Update best split if this is better
                if info_gain > max_info_gain:
                    max_info_gain = info_gain
                    self.j_best = j
                    self.t_best = t
                    self.y_hat_yes = utils.mode(y_yes)
                    self.y_hat_no = utils.mode(y_no)

    def predict(self, X):
        n = X.shape[0]

        if self.j_best is None:
            # Fallback if no split was found
            return np.zeros(n)

        y_hat = np.zeros(n)

        # Apply the learned decision rule
        yes_mask = X[:, self.j_best] >= self.t_best
        y_hat[yes_mask] = self.y_hat_yes
        y_hat[~yes_mask] = self.y_hat_no

        return y_hat



