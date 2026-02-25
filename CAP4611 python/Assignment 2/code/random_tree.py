from random_stump import RandomStumpInfoGain
from decision_tree import DecisionTree
import numpy as np

import utils


class RandomTree(DecisionTree):
    def __init__(self, max_depth):
        DecisionTree.__init__(
            self, max_depth=max_depth, stump_class=RandomStumpInfoGain
        )

    def fit(self, X, y):
        n = X.shape[0]
        boostrap_inds = np.random.choice(n, n, replace=True)
        bootstrap_X = X[boostrap_inds]
        bootstrap_y = y[boostrap_inds]

        DecisionTree.fit(self, bootstrap_X, bootstrap_y)


class RandomForest:
    """
    YOUR CODE HERE FOR Q4
    Hint: start with the constructor __init__(), which takes the hyperparameters.
    Hint: you can instantiate objects inside fit().
    Make sure predict() is able to handle multiple examples.
    """

    def __init__(self, num_trees, max_depth):
        self.num_trees = num_trees
        self.max_depth = max_depth
        self.trees = []


    def fit(self, X, y):
        self.trees = []

        for i in range(self.num_trees):
            # Create a new RandomTree
            tree = RandomTree(max_depth=self.max_depth)

            # Fit the tree to the data (RandomTree already handles bootstrap sampling)
            tree.fit(X, y)

            # Add to our forest
            self.trees.append(tree)

    def predict(self, X_pred):
        n = X_pred.shape[0]

        # Get predictions from all trees
        tree_predictions = np.zeros((self.num_trees, n))

        for i, tree in enumerate(self.trees):
            tree_predictions[i] = tree.predict(X_pred)

        # For each example, take the mode across all trees
        predictions = np.zeros(n)
        for i in range(n):
            predictions[i] = utils.mode(tree_predictions[:, i])

        return predictions

