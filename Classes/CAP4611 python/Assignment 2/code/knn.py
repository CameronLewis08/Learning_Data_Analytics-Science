"""
Implementation of k-nearest neighbours classifier
"""

import numpy as np

import utils
from utils import euclidean_dist_squared


class KNN:
    X = None
    y = None

    def __init__(self, k):
        self.k = k

    def fit(self, X, y):
        self.X = X  # just memorize the training data
        self.y = y

    def predict(self, X_hat):
        n_test = X_hat.shape[0]
        predictions = np.zeros(n_test)

        # Compute squared euclidean distances between test points and training points
        distances_squared = euclidean_dist_squared(X_hat, self.X)

        for i in range(n_test):
            # Get distances for the i-th test point
            distances_i = distances_squared[i, :]

            # Find indices of k nearest neighbors
            # argsort returns indices that would sort the array
            nearest_indices = np.argsort(distances_i)[:self.k]

            # Get labels of k nearest neighbors
            nearest_labels = self.y[nearest_indices]

            # Use mode to find most common label (handles ties correctly)
            predictions[i] = utils.mode(nearest_labels)

        return predictions

