import numpy as np


def f_noisy(x, n, q):
    if q == 0:
        assert np.random.binomial(x, 1 - q / n) + np.random.binomial(n - x, q / n) == x
    return np.random.binomial(x, 1 - q / n) + np.random.binomial(n - x, q / n)


def mutation(n, lam, q, x):
    l = np.random.binomial(n, lam / n)
    x_mutated_best = 0
    fx_mutated_best_noisy = -n
    m_0_best, m_1_best = 0, 0
    fitness_evaluations = 0

    for _ in range(lam):
        if l > 0:
            m_1 = np.random.hypergeometric(x, n - x, l)
            m_0 = l - m_1
            assert 0 <= m_0 <= l and m_0 <= n - x
            assert 0 <= m_1 <= l and m_1 <= x
        else:
            m_0, m_1 = 0, 0
        y = x - m_1 + m_0
        assert 0 <= y <= n
        fy_noisy = f_noisy(y, n, q)
        fitness_evaluations += 1

        if fy_noisy > fx_mutated_best_noisy:
            x_mutated_best = y
            fx_mutated_best_noisy = fy_noisy
            m_0_best, m_1_best = m_0, m_1

    return x_mutated_best, fx_mutated_best_noisy, m_0_best, m_1_best, fitness_evaluations


def crossover(n, lam, q, x, m_0, m_1):
    y_crossover_best = 0
    fy_crossover_best_noisy = -n
    fitness_evaluations = 0

    for _ in range(lam):
        y = x - m_1 + np.random.binomial(m_1, 1 - 1 / lam) + np.random.binomial(m_0, 1 / lam)
        assert 0 <= y <= n
        fy_noisy = f_noisy(y, n, q)
        fitness_evaluations += 1

        if fy_noisy > fy_crossover_best_noisy:
            y_crossover_best = y
            fy_crossover_best_noisy = fy_noisy

    return y_crossover_best, fy_crossover_best_noisy, fitness_evaluations


def algorithm(n, lam, q, algo_fun, fitness_evaluations):
    n_iters = 0
    x = np.random.binomial(n, 1 / 2)
    assert 0 <= x <= n
    n_iters_max = n ** 3

    while x != n and n_iters < n_iters_max:
        y, fy_noisy, fitness_evaluations_actual = algo_fun(n, lam, q, x)
        assert 0 <= y <= n

        if f_noisy(x, n, q) <= fy_noisy:
            x = y
        fitness_evaluations_actual += 1

        n_iters += 1
        assert fitness_evaluations == fitness_evaluations_actual

    return n_iters * fitness_evaluations


def ollga(n, lam, q):
    def algo_fun(n, lam, q, x):
        _, _, m_0, m_1, fitness_evaluations_1 = mutation(n, lam, q, x)
        y, fy_noisy, fitness_evaluations_2 = crossover(n, lam, q, x, m_0, m_1)
        return y, fy_noisy, fitness_evaluations_1 + fitness_evaluations_2

    return algorithm(n, lam, q, algo_fun, 2 * lam + 1)


def lea(n, lam, q):
    def algo_fun(n, lam, q, x):
        x_mutated, fx_noisy, _, _, fitness_evaluations = mutation(n, lam, q, x)
        return x_mutated, fx_noisy, fitness_evaluations

    return algorithm(n, lam, q, algo_fun, lam + 1)


def tlea(n, lam, q):
    def algo_fun(n, lam, q, x):
        x_mutated, fx_noisy, _, _, fitness_evaluations = mutation(n, lam, q, x)
        return x_mutated, fx_noisy, fitness_evaluations

    return algorithm(n, 2 * lam, q, algo_fun, 2 * lam + 1)
