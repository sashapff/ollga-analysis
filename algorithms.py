import numpy as np


def onemax(x, n, q, _):
    f_x_noisy = np.random.binomial(x, 1 - q / n) + np.random.binomial(n - x, q / n)
    if q == 0:
        assert f_x_noisy == x
    return f_x_noisy


def jump(x, n, q, k):
    f_x_noisy = onemax(x, n, q, k)
    if n - k < f_x_noisy < n:
        return -f_x_noisy
    else:
        return f_x_noisy


def lea_mutation(n, lam, q, f, k, p, x):
    if not p:
        p = 1 / n
    assert 0 <= p <= 1
    x_mutated_best = 0
    fx_mutated_best_noisy = -n
    fitness_evaluations = 0

    for _ in range(lam):
        m_1 = np.random.binomial(x, p)
        m_0 = np.random.binomial(n - x, p)
        assert 0 <= m_0 <= n - x
        assert 0 <= m_1 <= x
        y = x - m_1 + m_0
        assert 0 <= y <= n
        fy_noisy = f(y, n, q, k)
        fitness_evaluations += 1

        if fy_noisy > fx_mutated_best_noisy:
            x_mutated_best = y
            fx_mutated_best_noisy = fy_noisy

    return x_mutated_best, fx_mutated_best_noisy, fitness_evaluations


def ollga_mutation(n, lam, q, f, k, p, x):
    if not p:
        p = lam / n
    assert 0 <= p <= 1
    l = np.random.binomial(n, p)
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
        fy_noisy = f(y, n, q, k)
        fitness_evaluations += 1

        if fy_noisy > fx_mutated_best_noisy:
            x_mutated_best = y
            fx_mutated_best_noisy = fy_noisy
            m_0_best, m_1_best = m_0, m_1

    return m_0_best, m_1_best, fitness_evaluations


def crossover(n, lam, q, f, k, c, x, m_0, m_1):
    if not c:
        c = 1 / lam
    assert 0 <= c <= 1
    y_crossover_best = 0
    fy_crossover_best_noisy = -n
    fitness_evaluations = 0

    for _ in range(lam):
        y = x - m_1 + np.random.binomial(m_1, 1 - c) + np.random.binomial(m_0, c)
        assert 0 <= y <= n
        fy_noisy = f(y, n, q, k)
        fitness_evaluations += 1

        if fy_noisy > fy_crossover_best_noisy:
            y_crossover_best = y
            fy_crossover_best_noisy = fy_noisy

    return y_crossover_best, fy_crossover_best_noisy, fitness_evaluations


def algorithm(n, lam, q, algo_fun, f, k, p, c, fitness_evaluations):
    n_iters = 0
    x = np.random.binomial(n, 1 / 2)
    assert 0 <= x <= n
    n_iters_max = n ** 3

    while x != n and n_iters < n_iters_max:
        y, fy_noisy, fitness_evaluations_actual = algo_fun(n, lam, q, f, k, p, c, x)
        assert 0 <= y <= n

        if f(x, n, q, k) <= fy_noisy:
            x = y
        fitness_evaluations_actual += 1

        n_iters += 1
        assert fitness_evaluations == fitness_evaluations_actual

    return n_iters * fitness_evaluations


def ollga(n, lam, q, f, k, p, c):
    def algo_fun(n, lam, q, f, k, p, c, x):
        m_0, m_1, fitness_evaluations_1 = ollga_mutation(n, lam, q, f, k, p, x)
        y, fy_noisy, fitness_evaluations_2 = crossover(n, lam, q, f, k, c, x, m_0, m_1)
        return y, fy_noisy, fitness_evaluations_1 + fitness_evaluations_2

    return algorithm(n, lam, q, algo_fun, f, k, p, c, 2 * lam + 1)


def lea(n, lam, q, f, k, p, c):
    def algo_fun(n, lam, q, f, k, p, c, x):
        x_mutated, fx_noisy, fitness_evaluations = lea_mutation(n, lam, q, f, k, p, x)
        return x_mutated, fx_noisy, fitness_evaluations

    return algorithm(n, lam, q, algo_fun, f, k, p, c, lam + 1)


def tlea(n, lam, q, f, k, p, c):
    def algo_fun(n, lam, q, f, k, p, c, x):
        x_mutated, fx_noisy, fitness_evaluations = lea_mutation(n, lam, q, f, k, p, x)
        return x_mutated, fx_noisy, fitness_evaluations

    return algorithm(n, 2 * lam, q, algo_fun, f, k, p, c, 2 * lam + 1)
