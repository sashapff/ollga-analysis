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
    x_mutated = 0

    for _ in range(lam):
        y = x
        idx = np.random.choice(n, l, replace=False)
        for i in idx:
            y = flip(y, int(i))
        assert bin(x ^ y).count('1') == l

        if f_noisy(y, n, q) > f_noisy(x_mutated, n, q):
            x_mutated = y

    return x_mutated


def crossover(n, lam, q, x, x_mutated):
    y_crossover = 0
    for _ in range(lam):
        y = x
        for i in range(n):
            if (x ^ x_mutated) & (1 << i) != 0 and np.random.uniform() < 1 / lam:
                y = flip(y, i)

        if f_noisy(y, n, q) > f_noisy(y_crossover, n, q):
            y_crossover = y

    return y_crossover


def algorithm(n, lam, q, algo_fun):
    n_iters = 0
    best_x = (1 << n) - 1
    x = random.randint(0, best_x)
    n_iters_max = n ** 3
    while x != best_x and n_iters < n_iters_max:
        y = algo_fun(n, lam, q, x)

        if f_noisy(x, n, q) <= f_noisy(y, n, q):
            x = y

        n_iters += 1
    return n_iters


def ollga(n, lam, q):
    def algo_fun(n, lam, q, x):
        x_mutated = mutation(n, lam, q, x)
        return crossover(n, lam, q, x, x_mutated)

    return algorithm(n, lam, q, algo_fun)


def oplea(n, lam, q):
    def algo_fun(n, lam, q, x):
        return mutation(n, lam, q, x)

    return algorithm(n, lam, q, algo_fun)