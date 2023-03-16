import numpy as np
import matplotlib.pyplot as plt

def SPHERE(X):
    """
    Sphere benchmark function d-dimension

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += X_I ** 2
    OF = SUM
    return OF

def ROSENBROCK(X):
    """
    Rosenbrock benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM - 1):
        X_I = X[I_COUNT]
        X_NEXT = X[I_COUNT + 1]
        NEW = 100 * (X_NEXT - X_I ** 2) ** 2 + (X_I - 1) ** 2
        SUM += NEW
    OF = SUM
    return OF

def RASTRIGIN(X):
    """
    Rastrigin benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += (X_I ** 2 - 10 * np.cos(2 * np.pi * X_I))
    OF = 10 * DIM + SUM
    return OF

def ACKLEY(X):
    """
    Ackley benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    DIM = len(X)
    SUM1 = 0
    SUM2 = 0
    A = 20
    B = 0.2
    C = 2 * np.pi
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM1 += X_I ** 2
        SUM2 += np.cos(C * X_I)
    TERM_1 = -A * np.exp(-B * np.sqrt(SUM1 / DIM))
    TERM_2 = -np.exp(SUM2 / DIM)
    OF = TERM_1 + TERM_2 + A + np.exp(1)
    return OF

def GRIEWANK(X):
    """
    Griewank benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    DIM = len(X)
    SUM = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += (X_I ** 2) / 4000
    PROD = np.cos(X_I / np.sqrt(abs(X_I)))
    OF = SUM - PROD + 1
    return OF

def ZAKHAROV(X):
    """
    Zakharov benchmark function d-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    DIM = len(X)
    SUM_1 = 0
    SUM_2 = 0
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM_1 += X_I ** 2
        SUM_2 += (0.5 * I_COUNT * X_I)
    OF = SUM_1 + SUM_2**2 + SUM_2**4
    return OF

def EASOM(X):
    """
    Easom benchmark function 2-dimension

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    X_1 = X[0]
    X_2 = X[1]
    FACT_1 = - np.cos(X_1) * np.cos(X_2)
    FACT_2 = np.exp(- (X_1 - np.pi) ** 2 - (X_2 - np.pi) ** 2)
    OF = FACT_1 * FACT_2
    return OF

def MICHALEWICS(X):
    """
    Sphere benchmark function 2-dimension, 5-dimension and 10-dimension.

    See documentation in https://wmpjrufg.github.io/META_TOOLBOX/BENCHMARKS.html
    """

    DIM = len(X)
    SUM = 0
    M = 10
    for I_COUNT in range(DIM):
        X_I = X[I_COUNT]
        SUM += np.sin(X_I) * (np.sin((I_COUNT * X_I ** 2) / np.pi)**(2 * M))
    OF = - SUM
    return OF

def PLOT_BENCHMARK(X,FUNCTION,X_L, X_U):
    N = 100
    X_AUX = np.linspace(X_L, X_U, N)
    Y_AUX = np.linspace(X_L, X_U, N)
    A, B = np.meshgrid(X_AUX, Y_AUX)
    Z = np.zeros((N,N))
    for I in range(N):
        for J in range(N):
            X = [A[I, J], B[I, J]]
            if FUNCTION == "ACKLEY":
                Z[I, J] = ACKLEY(X)
            if FUNCTION == "SPHERE":
                Z[I, J] = SPHERE(X)
            if FUNCTION == "ROSENBROCK":
                Z[I, J] = ROSENBROCK(X)
            if FUNCTION == "RASTRIGIN":
                Z[I, J] = RASTRIGIN(X)
            if FUNCTION == "GRIEWANK":
                Z[I, J] = GRIEWANK(X)
            if FUNCTION == "ZAKHAROV":
                Z[I, J] = ZAKHAROV(X)
            if FUNCTION == "EASOM":
                Z[I, J] = EASOM(X)
            if FUNCTION == "MICHALEWICS":
                Z[I, J] = MICHALEWICS(X)
    fig = plt.figure(figsize=(5, 5))
    # plt.title(FUNCTION)
    # ax.zaxis.set_major_formatter('{x:.0f}')

    plt.rc('font', size=6)
    ax = plt.axes(projection='3d')
    ax.contour3D(A, B, Z, 100, cmap='jet')
    fig.set_facecolor('black')
    ax.set_facecolor('black')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z');
