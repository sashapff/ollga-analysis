import numpy as np
import random


def f(x):
    return bin(x).count('1')


def flip(x, i):
    return x ^ (1 << i)


def f_noisy(x, n, q):
    x_noisy = x
    for i in range(n):
        if np.random.uniform() < q / n:
            x_noisy = flip(x_noisy, i)
    return f(x_noisy)


def mutation(n, lam, q, x):
    l = np.random.binomial(n, lam / n)
    x_mutated = x
    f_x_mutated = f_noisy(x, n, q)

    for _ in range(lam):
        y = x
        idx = np.random.choice(n, l, replace=False)
        for i in idx:
            y = flip(y, int(i))

        f_y = f_noisy(y, n, q)

        if f_y > f_x_mutated:
            x_mutated = y
        f_x_mutated = f_noisy(x_mutated, n, q)

    return x_mutated, f_x_mutated


def crossover(n, lam, q, x, x_mutated):
    y_crossover = x
    f_y_crossover = f_noisy(y_crossover, n, q)
    for _ in range(lam):
        y = x
        for i in range(n):
            if x ^ (1 << i) != x_mutated ^ (1 << i) and np.random.uniform() < 1 / lam:
                y = flip(y, i)

        f_y = f_noisy(y, n, q)

        if f_y > f_y_crossover:
            y_crossover = y
        f_y_crossover = f_noisy(y_crossover, n, q)

    return y_crossover, f_y_crossover


def algorithm(n, lam, q, algo_fun):
    n_iters = 0
    x = random.randint(0, 1 << n - 1)
    f_x = f_noisy(x, n, q)
    n_iters_max = n ** 3
    while f(x) != n and n_iters < n_iters_max:
        y, f_y = algo_fun(n, lam, q, x)

        if f_x <= f_y:
            x = y
        f_x = f_noisy(x, n, q)

        n_iters += 1
    return n_iters


def ollga(n, lam, q):
    def algo_fun(n, lam, q, x):
        x_mutated, _ = mutation(n, lam, q, x)
        return crossover(n, lam, q, x, x_mutated)

    return algorithm(n, lam, q, algo_fun)


def oplea(n, lam, q):
    def algo_fun(n, lam, q, x):
        return mutation(n, lam, q, x)

    return algorithm(n, lam, q, algo_fun)