#!/usr/bin/env python
import argparse
import os
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# make sure we're working in the directory this file lives in,
# for imports and for simplicity with relative paths
os.chdir(Path(__file__).parent.resolve())

# our code
from utils import load_dataset, plot_classifier, handle, run, main
from decision_stump import DecisionStumpInfoGain
from decision_tree import DecisionTree
from kmeans import Kmeans
from knn import KNN
from naive_bayes import NaiveBayes, NaiveBayesLaplace
from random_tree import RandomForest, RandomTree


@handle("1")
def q1():
    dataset = load_dataset("citiesSmall.pkl")

    X = dataset["X"]
    y = dataset["y"]
    X_test = dataset["Xtest"]
    y_test = dataset["ytest"]

    # Test k-NN for k = 1, 3, and 10
    k_values = [1, 3, 10]

    print("KNN Results:")
    for k in k_values:
        model = KNN(k=k)
        model.fit(X, y)

        # Training error
        y_pred_train = model.predict(X)
        train_error = np.mean(y_pred_train != y)

        # Test error
        y_pred_test = model.predict(X_test)
        test_error = np.mean(y_pred_test != y_test)

        print(f"k={k} Training error = {train_error:.3f} Test error = {test_error:.3f}")

    # Optional: Compare with Decision Tree
    print("\nDecision Tree comparison:")
    dt_model = DecisionTreeClassifier()
    dt_model.fit(X, y)
    dt_train_error = np.mean(dt_model.predict(X) != y)
    dt_test_error = np.mean(dt_model.predict(X_test) != y_test)
    print(f"Decision Tree: Training error = {dt_train_error:.3f}, Test error = {dt_test_error:.3f}")

    # Generate plot for k=1
    model_k1 = KNN(k=1)
    model_k1.fit(X, y)

    plt.figure(figsize=(8, 6))
    plot_classifier(model_k1, X, y)
    plt.title("k-NN Classification with k=1")
    plt.savefig("../figs/knn_k1_plot.png")
    print("Plot saved as ../figs/knn_k1_plot.png")


@handle("2")
def q2():
    dataset = load_dataset("ccdebt.pkl")
    X = dataset["X"]
    y = dataset["y"]
    X_test = dataset["Xtest"]
    y_test = dataset["ytest"]

    ks = list(range(1, 30, 4))

    n = X.shape[0]

    # Implement 10-fold cross-validation
    fold_size = n // 10
    cv_accs = []
    test_accs = []
    train_accs = []

    for k in ks:
        # Cross-validation accuracies for this k
        fold_accs = []

        for fold in range(10):
            # Create mask for this fold
            mask = np.ones(n, dtype=bool)
            start_idx = fold * fold_size
            if fold == 9:  # Last fold gets any remaining examples
                end_idx = n
            else:
                end_idx = (fold + 1) * fold_size

            # Set validation indices to False
            mask[start_idx:end_idx] = False

            # Split data
            X_train_fold = X[mask]
            y_train_fold = y[mask]
            X_val_fold = X[~mask]
            y_val_fold = y[~mask]

            # Train and evaluate
            model = KNN(k=k)
            model.fit(X_train_fold, y_train_fold)
            y_pred_val = model.predict(X_val_fold)
            fold_accuracy = np.mean(y_pred_val == y_val_fold)
            fold_accs.append(fold_accuracy)

        # Store mean accuracy across folds
        cv_accs.append(np.mean(fold_accs))

        # Also compute test accuracy for comparison
        model_full = KNN(k=k)
        model_full.fit(X, y)

        # Training accuracy
        y_pred_train = model_full.predict(X)
        train_accuracy = np.mean(y_pred_train == y)
        train_accs.append(train_accuracy)

        # Test accuracy
        y_pred_test = model_full.predict(X_test)
        test_accuracy = np.mean(y_pred_test == y_test)
        test_accs.append(test_accuracy)

    # Plot cross-validation and test accuracies
    plt.figure(figsize=(10, 6))
    plt.plot(ks, cv_accs, 'b-o', label='Cross-validation accuracy')
    plt.plot(ks, test_accs, 'r-s', label='Test accuracy')
    plt.xlabel('k')
    plt.ylabel('Accuracy')
    plt.title('Cross-validation vs Test Accuracy')
    plt.legend()
    plt.grid(True)
    plt.savefig("../figs/cv_vs_test_accuracy.png")
    print("CV vs Test accuracy plot saved as ../figs/cv_vs_test_accuracy.png")

    # Plot training error
    plt.figure(figsize=(10, 6))
    train_errors = [1 - acc for acc in train_accs]
    plt.plot(ks, train_errors, 'g-^', label='Training error')
    plt.xlabel('k')
    plt.ylabel('Training Error')
    plt.title('Training Error vs k')
    plt.legend()
    plt.grid(True)
    plt.savefig("../figs/training_error_vs_k.png")
    print("Training error plot saved as ../figs/training_error_vs_k.png")

    # Find best k values
    best_cv_k = ks[np.argmax(cv_accs)]
    best_test_k = ks[np.argmax(test_accs)]

    print(f"\nResults:")
    print(f"Best k according to cross-validation: {best_cv_k} (CV accuracy: {max(cv_accs):.3f})")
    print(f"Best k according to test accuracy: {best_test_k} (Test accuracy: {max(test_accs):.3f})")
    print(f"CV-chosen k test accuracy: {test_accs[ks.index(best_cv_k)]:.3f}")



@handle("3.2")
def q3_2():
    dataset = load_dataset("newsgroups.pkl")

    X = dataset["X"].astype(bool)
    y = dataset["y"]
    X_valid = dataset["Xvalidate"]
    y_valid = dataset["yvalidate"]
    groupnames = dataset["groupnames"]
    wordlist = dataset["wordlist"]

    """YOUR CODE HERE FOR Q3.2"""
    word_73 = wordlist[72]
    print(f"1. Word at column 73 (index 72): {word_73}")

    # 2. Which words are present in training example 803 (index 802)?
    example_803_features = X[802]
    present_words = [wordlist[i] for i in range(len(wordlist)) if example_803_features[i] == 1]
    print(f"2. Words present in example 803: {present_words}")

    # 3. Which newsgroup does example 803 come from?
    example_803_group = groupnames[y[802]]
    print(f"3. Example 803 belongs to newsgroup: {example_803_group}")



@handle("3.3")
def q3_3():
    dataset = load_dataset("newsgroups.pkl")

    X = dataset["X"]
    y = dataset["y"]
    X_valid = dataset["Xvalidate"]
    y_valid = dataset["yvalidate"]

    print(f"d = {X.shape[1]}")
    print(f"n = {X.shape[0]}")
    print(f"t = {X_valid.shape[0]}")
    print(f"Num classes = {len(np.unique(y))}")

    """CODE FOR Q3.4: Modify naive_bayes.py/NaiveBayesLaplace"""

    model = NaiveBayes(num_classes=4)
    model.fit(X, y)

    y_hat = model.predict(X)
    err_train = np.mean(y_hat != y)
    print(f"Naive Bayes training error: {err_train:.3f}")

    y_hat = model.predict(X_valid)
    err_valid = np.mean(y_hat != y_valid)
    print(f"Naive Bayes validation error: {err_valid:.3f}")


@handle("3.4")
def q3_4():
    dataset = load_dataset("newsgroups.pkl")

    X = dataset["X"]
    y = dataset["y"]
    X_valid = dataset["Xvalidate"]
    y_valid = dataset["yvalidate"]

    print(f"d = {X.shape[1]}")
    print(f"n = {X.shape[0]}")
    print(f"t = {X_valid.shape[0]}")
    print(f"Num classes = {len(np.unique(y))}")

    model = NaiveBayes(num_classes=4)
    model.fit(X, y)

    """YOUR CODE HERE FOR Q3.4. Also modify naive_bayes.py/NaiveBayesLaplace"""
    # Compare regular Naive Bayes with Laplace smoothing
    model_laplace = NaiveBayesLaplace(num_classes=4, beta=1)
    model_laplace.fit(X, y)

    # Look at p(x_ij = 1 | y_i = 0) for all features j in both models
    regular_probs = model.p_xy[:, 0]  # All features for class 0
    laplace_probs = model_laplace.p_xy[:, 0]  # All features for class 0

    print(f"\nRegular Naive Bayes - min prob: {np.min(regular_probs):.6f}, max prob: {np.max(regular_probs):.6f}")
    print(f"Laplace smoothing (β=1) - min prob: {np.min(laplace_probs):.6f}, max prob: {np.max(laplace_probs):.6f}")

    # Check if any probabilities are exactly 0 in regular NB
    zero_probs = np.sum(regular_probs == 0)
    print(f"Number of zero probabilities in regular NB: {zero_probs}")
    print("Difference: Laplace smoothing prevents zero probabilities which can cause numerical issues.")

    # Try with very large beta
    model_large_beta = NaiveBayesLaplace(num_classes=4, beta=10000)
    model_large_beta.fit(X, y)
    large_beta_probs = model_large_beta.p_xy[:, 0]

    print(
        f"\nLaplace with β=10000 - min prob: {np.min(large_beta_probs):.6f}, max prob: {np.max(large_beta_probs):.6f}")
    print("With very large β, all probabilities approach 0.5, as the smoothing dominates the actual data.")

    # Report training and validation errors for comparison
    y_hat_train = model.predict(X)
    err_train = np.mean(y_hat_train != y)
    print(f"\nNaive Bayes training error: {err_train:.3f}")

    y_hat_valid = model.predict(X_valid)
    err_valid = np.mean(y_hat_valid != y_valid)
    print(f"Naive Bayes validation error: {err_valid:.3f}")

    # Laplace smoothing results
    y_hat_train_lap = model_laplace.predict(X)
    err_train_lap = np.mean(y_hat_train_lap != y)
    print(f"Naive Bayes Laplace training error: {err_train_lap:.3f}")

    y_hat_valid_lap = model_laplace.predict(X_valid)
    err_valid_lap = np.mean(y_hat_valid_lap != y_valid)
    print(f"Naive Bayes Laplace validation error: {err_valid_lap:.3f}")



@handle("4")
def q4():
    dataset = load_dataset("vowel.pkl")
    X = dataset["X"]
    y = dataset["y"]
    X_test = dataset["Xtest"]
    y_test = dataset["ytest"]
    print(f"n = {X.shape[0]}, d = {X.shape[1]}")

    def evaluate_model(model):
        model.fit(X, y)

        y_pred = model.predict(X)
        tr_error = np.mean(y_pred != y)

        y_pred = model.predict(X_test)
        te_error = np.mean(y_pred != y_test)
        print(f"    Training error: {tr_error:.3f}")
        print(f"    Testing error: {te_error:.3f}")

    print("Decision tree info gain")
    evaluate_model(DecisionTree(max_depth=np.inf, stump_class=DecisionStumpInfoGain))

    """YOUR CODE FOR Q4. Also modify random_tree.py/RandomForest"""

    print("\nRandom tree")
    evaluate_model(RandomTree(max_depth=np.inf))

    print("\nRandom Forest (50 trees, max_depth=∞)")
    evaluate_model(RandomForest(num_trees=50, max_depth=np.inf))

    print("\nAnswers to questions:")
    print("Q4.1: RandomTree doesn't have 0 training error because it uses random feature")
    print("      selection and bootstrap sampling, which introduces randomness.")
    print("Q4.2: Training terminates because eventually no split improves the criterion,")
    print("      or all examples in a node have the same label.")
    print("Q4.5: Random forests typically have 0 training error because with enough trees,")
    print("      the ensemble can memorize the training data, even though individual")
    print("      trees have training error > 0.")



@handle("5")
def q5():
    X = load_dataset("clusterData.pkl")["X"]

    model = Kmeans(k=4)
    model.fit(X)
    y = model.predict(X)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap="jet")

    fname = Path("..", "figs", "kmeans_basic_rerun.png")
    plt.savefig(fname)
    print(f"Figure saved as {fname}")


@handle("5.1")
def q5_1():
    X = load_dataset("clusterData.pkl")["X"]

    """YOUR CODE HERE FOR Q5.1. Also modify kmeans.py/Kmeans"""

    best_error = float('inf')
    best_model = None
    errors = []

    for i in range(50):
        model = Kmeans(k=4)
        model.fit(X)
        y_pred = model.predict(X)
        error = model.error(X, y_pred, model.means)
        errors.append(error)

        if error < best_error:
            best_error = error
            best_model = model

    print(f"Lowest error obtained: {best_error:.3f}")

    # Visualize the best clustering
    y_best = best_model.predict(X)
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y_best, cmap="jet")
    plt.title(f'Best K-means Clustering (Error: {best_error:.3f})')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')

    fname = Path("..", "figs", "kmeans_best_clustering.png")
    plt.savefig(fname)
    print(f"Best clustering plot saved as {fname}")

    print("The error decreases with each iteration because k-means minimizes")
    print("the sum of squared distances objective function.")



@handle("5.2")
def q5_2():
    X = load_dataset("clusterData.pkl")["X"]

    """YOUR CODE HERE FOR Q5.2"""

    k_values = range(1, 11)
    min_errors = []

    for k in k_values:
        errors_for_k = []

        # Run 50 times for each k
        for i in range(50):
            model = Kmeans(k=k)
            model.fit(X)
            y_pred = model.predict(X)
            error = model.error(X, y_pred, model.means)
            errors_for_k.append(error)

        min_error = min(errors_for_k)
        min_errors.append(min_error)
        print(f"k={k}: min error = {min_error:.3f}")

    # Plot the elbow curve
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, min_errors, 'bo-')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Minimum error across 50 runs')
    plt.title('Elbow Method for Choosing k')
    plt.grid(True)

    fname = Path("..", "figs", "elbow_method.png")
    plt.savefig(fname)
    print(f"Elbow method plot saved as {fname}")

    print("\nAnswers to questions:")
    print("Q5.2.1: We shouldn't choose k by minimizing error because error always")
    print("        decreases as k increases (k=n gives error=0).")
    print("Q5.2.2: No, validation data isn't suitable for choosing k in clustering")
    print("        because clustering is unsupervised - we don't have labels.")
    print("Q5.2.4: Reasonable k values by elbow method: k=3 or k=4")
    print("        (look for the 'elbow' where error reduction rate decreases)")



if __name__ == "__main__":
    main()
