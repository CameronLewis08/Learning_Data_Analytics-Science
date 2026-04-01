#!/usr/bin/env python
import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# make sure we're working in the directory this file lives in,
# for imports and for simplicity with relative paths
os.chdir(Path(__file__).parent.resolve())

from encoders import PCAEncoder
from kernels import GaussianRBFKernel, LinearKernel, PolynomialKernel
from linear_models import (
    LinearModel,
    LinearClassifier,
    KernelClassifier,
)
from optimizers import (
    GradientDescent,
    GradientDescentLineSearch,
    StochasticGradient,
)
from fun_obj import (
    LeastSquaresLoss,
    LogisticRegressionLossL2,
    KernelLogisticRegressionLossL2,
)
from learning_rate_getters import (
    ConstantLR,
    InverseLR,
    InverseSqrtLR,
    InverseSquaredLR,
)
from utils import (
    load_dataset,
    load_trainval,
    load_and_split,
    plot_classifier,
    savefig,
    standardize_cols,
    handle,
    run,
    main,
)


@handle("1")
def q1():
    X_train, y_train, X_val, y_val = load_and_split("nonLinearData.pkl")

    # Standard (regularized) logistic regression
    loss_fn = LogisticRegressionLossL2(1)
    optimizer = GradientDescentLineSearch()
    lr_model = LinearClassifier(loss_fn, optimizer)
    lr_model.fit(X_train, y_train)

    print(f"Training error {np.mean(lr_model.predict(X_train) != y_train):.1%}")
    print(f"Validation error {np.mean(lr_model.predict(X_val) != y_val):.1%}")

    fig = plot_classifier(lr_model, X_train, y_train)
    savefig("logRegPlain.png", fig)

    # kernel logistic regression with a linear kernel
    loss_fn = KernelLogisticRegressionLossL2(1)
    optimizer = GradientDescentLineSearch()
    kernel = LinearKernel()
    klr_model = KernelClassifier(loss_fn, optimizer, kernel)
    klr_model.fit(X_train, y_train)

    print(f"Training error {np.mean(klr_model.predict(X_train) != y_train):.1%}")
    print(f"Validation error {np.mean(klr_model.predict(X_val) != y_val):.1%}")

    fig = plot_classifier(klr_model, X_train, y_train)
    savefig("logRegLinear.png", fig)


@handle("1.1")
def q1_1():
    X_train, y_train, X_val, y_val = load_and_split("nonLinearData.pkl")

    """YOUR CODE HERE FOR Q1.1"""
    loss_fn = KernelLogisticRegressionLossL2(lammy=0.01)
    optimizer = GradientDescentLineSearch()
    kernel = PolynomialKernel(p=2)
    model = KernelClassifier(loss_fn, optimizer, kernel)
    model.fit(X_train, y_train)

    print(f"Polynomial Kernel (p=2):")
    print(f"Training error {np.mean(model.predict(X_train) != y_train):.1%}")
    print(f"Validation error {np.mean(model.predict(X_val) != y_val):.1%}")

    fig = plot_classifier(model, X_train, y_train)
    savefig("logRegPoly.png", fig)

    # RBF kernel with σ=0.5
    kernel = GaussianRBFKernel(sigma=0.5)
    model = KernelClassifier(loss_fn, optimizer, kernel)
    model.fit(X_train, y_train)

    print(f"\nGaussian RBF Kernel (σ=0.5):")
    print(f"Training error {np.mean(model.predict(X_train) != y_train):.1%}")
    print(f"Validation error {np.mean(model.predict(X_val) != y_val):.1%}")

    fig = plot_classifier(model, X_train, y_train)
    savefig("logRegRBF.png", fig)


@handle("1.2")
def q1_2():
    X_train, y_train, X_val, y_val = load_and_split("nonLinearData.pkl")

    sigmas = 10.0 ** np.array([-2, -1, 0, 1, 2])
    lammys = 10.0 ** np.array([-4, -3, -2, -1, 0, 1, 2])

    # train_errs[i, j] should be the train error for sigmas[i], lammys[j]
    train_errs = np.full((len(sigmas), len(lammys)), 100.0)
    val_errs = np.full((len(sigmas), len(lammys)), 100.0)  # same for val

    """YOUR CODE HERE FOR Q1.2"""
    for i, sigma in enumerate(sigmas):
        for j, lammy in enumerate(lammys):
            kernel = GaussianRBFKernel(sigma=sigma)
            loss_fn = KernelLogisticRegressionLossL2(lammy=lammy)
            optimizer = GradientDescentLineSearch()
            model = KernelClassifier(loss_fn, optimizer, kernel)
            model.fit(X_train, y_train)

            train_errs[i, j] = np.mean(model.predict(X_train) != y_train)
            val_errs[i, j] = np.mean(model.predict(X_val) != y_val)

        # Find best hyperparameters
    best_train_idx = np.unravel_index(np.argmin(train_errs), train_errs.shape)
    best_val_idx = np.unravel_index(np.argmin(val_errs), val_errs.shape)

    print(
        f"Best training: σ={sigmas[best_train_idx[0]]}, λ={lammys[best_train_idx[1]]}, error={train_errs[best_train_idx]:.1%}")
    print(
        f"Best validation: σ={sigmas[best_val_idx[0]]}, λ={lammys[best_val_idx[1]]}, error={val_errs[best_val_idx]:.1%}")

    # Train and plot model with best training error hyperparameters
    best_train_sigma = sigmas[best_train_idx[0]]
    best_train_lammy = lammys[best_train_idx[1]]
    kernel = GaussianRBFKernel(sigma=best_train_sigma)
    loss_fn = KernelLogisticRegressionLossL2(lammy=best_train_lammy)
    optimizer = GradientDescentLineSearch()
    model_best_train = KernelClassifier(loss_fn, optimizer, kernel)
    model_best_train.fit(X_train, y_train)

    fig = plot_classifier(model_best_train, X_train, y_train)
    savefig("logRegRBF_best_train.png", fig)
    plt.close(fig)

    # Train and plot model with best validation error hyperparameters
    best_val_sigma = sigmas[best_val_idx[0]]
    best_val_lammy = lammys[best_val_idx[1]]
    kernel = GaussianRBFKernel(sigma=best_val_sigma)
    loss_fn = KernelLogisticRegressionLossL2(lammy=best_val_lammy)
    optimizer = GradientDescentLineSearch()
    model_best_val = KernelClassifier(loss_fn, optimizer, kernel)
    model_best_val.fit(X_train, y_train)

    fig = plot_classifier(model_best_val, X_train, y_train)
    savefig("logRegRBF_best_val.png", fig)
    plt.close(fig)

    # Make a picture with the two error arrays. No need to worry about details here.
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
    norm = plt.Normalize(vmin=0, vmax=max(train_errs.max(), val_errs.max()))
    for (name, errs), ax in zip([("training", train_errs), ("val", val_errs)], axes):
        cax = ax.matshow(errs, norm=norm)

        ax.set_title(f"{name} errors")
        ax.set_ylabel(r"$\sigma$")
        ax.set_yticks(range(len(sigmas)))
        ax.set_yticklabels([str(sigma) for sigma in sigmas])
        ax.set_xlabel(r"$\lambda$")
        ax.set_xticks(range(len(lammys)))
        ax.set_xticklabels([str(lammy) for lammy in lammys])
        ax.xaxis.set_ticks_position("bottom")
    fig.colorbar(cax)
    savefig("logRegRBF_grids.png", fig)


@handle("3.2")
def q3_2():
    data = load_dataset("animals.pkl")
    X_train = data["X"]
    animal_names = data["animals"]
    trait_names = data["traits"]

    # Standardize features
    X_train_standardized, mu, sigma = standardize_cols(X_train)
    n, d = X_train_standardized.shape

    # Matrix plot
    fig, ax = plt.subplots()
    ax.imshow(X_train_standardized)
    savefig("animals_matrix.png", fig)
    plt.close(fig)

    # 2D visualization
    np.random.seed(3164)  # make sure you keep this seed
    j1, j2 = np.random.choice(d, 2, replace=False)  # choose 2 random features
    random_is = np.random.choice(n, 15, replace=False)  # choose random examples

    fig, ax = plt.subplots()
    ax.scatter(X_train_standardized[:, j1], X_train_standardized[:, j2])
    for i in random_is:
        xy = X_train_standardized[i, [j1, j2]]
        ax.annotate(animal_names[i], xy=xy)
    savefig("animals_random.png", fig)
    plt.close(fig)

    """YOUR CODE HERE FOR Q3"""
    pca = PCAEncoder(k=2)
    pca.fit(X_train_standardized)
    Z = pca.encode(X_train_standardized)

    fig, ax = plt.subplots()
    ax.scatter(Z[:, 0], Z[:, 1])
    for i in random_is:
        ax.annotate(animal_names[i], xy=Z[i, :])
    ax.set_xlabel('PC 1')
    ax.set_ylabel('PC 2')
    savefig("animals_pca.png", fig)

    # Find traits with largest influence
    print(f"Largest influence on PC1: {trait_names[np.argmax(np.abs(pca.W[0, :]))]}")
    print(f"Largest influence on PC2: {trait_names[np.argmax(np.abs(pca.W[1, :]))]}")


@handle("4")
def q4():
    X_train_orig, y_train, X_val_orig, y_val = load_trainval("dynamics.pkl")
    X_train, mu, sigma = standardize_cols(X_train_orig)
    X_val, _, _ = standardize_cols(X_val_orig, mu, sigma)

    # Train ordinary regularized least squares
    loss_fn = LeastSquaresLoss()
    optimizer = GradientDescentLineSearch()
    model = LinearModel(loss_fn, optimizer, check_correctness=False)
    model.fit(X_train, y_train)
    print(model.fs)  # ~700 seems to be the global minimum.

    print(f"Training MSE: {((model.predict(X_train) - y_train) ** 2).mean():.3f}")
    print(f"Validation MSE: {((model.predict(X_val) - y_val) ** 2).mean():.3f}")

    # Plot the learning curve!
    fig, ax = plt.subplots()
    ax.plot(model.fs, marker="o")
    ax.set_xlabel("Gradient descent iterations")
    ax.set_ylabel("Objective function f value")
    savefig("gd_line_search_curve.png", fig)


@handle("4.1")
def q4_1():
    X_train_orig, y_train, X_val_orig, y_val = load_trainval("dynamics.pkl")
    X_train, mu, sigma = standardize_cols(X_train_orig)
    X_val, _, _ = standardize_cols(X_val_orig, mu, sigma)

    """YOUR CODE HERE FOR Q4.1"""
    print("Reference (GD with line search):")
    loss_fn = LeastSquaresLoss()
    optimizer = GradientDescentLineSearch()
    model = LinearModel(loss_fn, optimizer, check_correctness=False)
    model.fit(X_train, y_train)
    print(f"Training MSE: {((model.predict(X_train) - y_train) ** 2).mean():.3f}")
    print(f"Validation MSE: {((model.predict(X_val) - y_val) ** 2).mean():.3f}")

    # SGD with different batch sizes
    batch_sizes = [1, 10, 100]

    for batch_size in batch_sizes:
        print(f"\nSGD with batch_size={batch_size}:")

        loss_fn = LeastSquaresLoss()
        base_optimizer = GradientDescent(max_evals=1)  # only 1 step per batch
        lr_getter = ConstantLR(multiplier=0.0003)
        optimizer = StochasticGradient(
            base_optimizer=base_optimizer,
            learning_rate_getter=lr_getter,
            batch_size=batch_size,
            max_evals=10  # 10 epochs
        )

        model = LinearModel(loss_fn, optimizer, check_correctness=False)
        model.fit(X_train, y_train)

        train_mse = ((model.predict(X_train) - y_train) ** 2).mean()
        val_mse = ((model.predict(X_val) - y_val) ** 2).mean()

        print(f"Training MSE: {train_mse:.3f}")
        print(f"Validation MSE: {val_mse:.3f}")


@handle("4.3")
def q4_3():
    X_train_orig, y_train, X_val_orig, y_val = load_trainval("dynamics.pkl")
    X_train, mu, sigma = standardize_cols(X_train_orig)
    X_val, _, _ = standardize_cols(X_val_orig, mu, sigma)

    """YOUR CODE HERE FOR Q4.3"""
    batch_size = 10
    multiplier = 0.1
    max_epochs = 50

    lr_classes = [
        ("Constant", ConstantLR),
        ("Inverse", InverseLR),
        ("Inverse Squared", InverseSquaredLR),
        ("Inverse Sqrt", InverseSqrtLR)
    ]

    fig, ax = plt.subplots(figsize=(10, 6))

    for name, LRClass in lr_classes:
        loss_fn = LeastSquaresLoss()
        base_optimizer = GradientDescent(max_evals=1)
        lr_getter = LRClass(multiplier=multiplier)
        optimizer = StochasticGradient(
            base_optimizer=base_optimizer,
            learning_rate_getter=lr_getter,
            batch_size=batch_size,
            max_evals=max_epochs,
            verbose=False
        )

        model = LinearModel(loss_fn, optimizer, check_correctness=False)
        model.fit(X_train, y_train)

        ax.plot(model.fs, marker='o', markersize=3, label=name)

    ax.set_xlabel("Epochs")
    ax.set_ylabel("Objective function f value")
    ax.set_title("SGD Learning Curves with Different Learning Rate Schedules")
    ax.legend()
    ax.grid(True, alpha=0.3)
    savefig("sgd_learning_curves.png", fig)

    print("\nWhich converge to global minimum?")
    print("Constant and Inverse Sqrt typically converge to the global minimum.")
    print("Inverse converges slowly but eventually reaches the minimum.")
    print("Inverse Squared decreases too fast and gets stuck at a suboptimal solution.")


if __name__ == "__main__":
    main()
