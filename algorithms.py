import numpy as np


def stop_criterion(n, filename=None):
    return n ** 10


def is_quick(f):
    return f == onemax or f == jump


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


def leading_ones(x, n, q, k):
    fx = 0
    for i in x:
        if np.random.uniform() < q / n:
            i ^= 1
        fx += i
        if i == 0:
            break
    return fx


def quick_lea_mutation(n, lam, q, f, k, p, x):
    if not p:
        p = 1 / n
    assert 0 <= p <= 1
    x_mutated_best = 0
    fx_mutated_best_noisy = -1e9 * n
    fitness_evaluations = 0

    for _ in range(lam):
        if is_quick(f):
            m_1 = np.random.binomial(x, p)
            m_0 = np.random.binomial(n - x, p)
            assert 0 <= m_0 <= n - x
            assert 0 <= m_1 <= x
            y = x - m_1 + m_0
            assert 0 <= y <= n
        else:
            y = x.copy()
            for i in range(n):
                if np.random.uniform() < p:
                    y[i] ^= 1
        fy_noisy = f(y, n, q, k)
        fitness_evaluations += 1

        if fy_noisy > fx_mutated_best_noisy:
            x_mutated_best = y
            fx_mutated_best_noisy = fy_noisy

    return x_mutated_best, fx_mutated_best_noisy, fitness_evaluations


def quick_ollga_mutation(n, lam, q, f, k, p, x):
    if not p:
        p = lam / n
    assert 0 <= p <= 1
    l = np.random.binomial(n, p)
    x_mutated_best = 0
    fx_mutated_best_noisy = -1e9 * n
    m_0_best, m_1_best = 0, 0
    fitness_evaluations = 0

    for _ in range(lam):
        m_0, m_1 = 0, 0
        if is_quick(f):
            if l > 0:
                m_1 = np.random.hypergeometric(x, n - x, l)
                m_0 = l - m_1
                assert 0 <= m_0 <= l and m_0 <= n - x
                assert 0 <= m_1 <= l and m_1 <= x
            else:
                m_0, m_1 = 0, 0
            y = x - m_1 + m_0
            assert 0 <= y <= n
        else:
            y = x.copy()
            for i in range(n):
                if np.random.uniform() < p:
                    y[i] ^= 1
        fy_noisy = f(y, n, q, k)
        fitness_evaluations += 1

        if fy_noisy > fx_mutated_best_noisy:
            x_mutated_best = y
            fx_mutated_best_noisy = fy_noisy
            m_0_best, m_1_best = m_0, m_1

    return m_0_best, m_1_best, fitness_evaluations, x_mutated_best


def crossover(n, lam, q, f, k, c, x, m_0, m_1, x_mutated):
    if not c:
        c = 1 / lam
    assert 0 <= c <= 1
    y_crossover_best = 0
    fy_crossover_best_noisy = -1e9 * n
    fitness_evaluations = 0

    for _ in range(lam):
        if is_quick(f):
            y = x - m_1 + np.random.binomial(m_1, 1 - c) + np.random.binomial(m_0, c)
            assert 0 <= y <= n
        else:
            y = x.copy()
            for i in range(n):
                if x[i] != x_mutated[i] and np.random.uniform() < 1 / lam:
                    y[i] ^= 1

        fy_noisy = f(y, n, q, k)
        fitness_evaluations += 1

        if fy_noisy > fy_crossover_best_noisy:
            y_crossover_best = y
            fy_crossover_best_noisy = fy_noisy

    return y_crossover_best, fy_crossover_best_noisy, fitness_evaluations


def not_find_optimum(x, n, f):
    if is_quick(f):
        return x != n
    else:
        return x.sum() != n


def algorithm(n, lam, q, algo_fun, f, k, p, c, fitness_evaluations, filename, reevaluate=True):
    n_iters = 0
    if is_quick(f):
        x = np.random.binomial(n, 1 / 2)
        assert 0 <= x <= n
    else:
        x = np.random.randint(0, 2, n)
    fx_noisy = f(x, n, q, k)

    n_iters_max = stop_criterion(n, filename)
    while not_find_optimum(x, n, f):
        y, fy_noisy, fitness_evaluations_actual = algo_fun(n, lam, q, f, k, p, c, x)

        if reevaluate:
            if f(x, n, q, k) <= fy_noisy:
                x = y
        else:
            if fx_noisy <= fy_noisy:
                x = y
                fx_noisy = fy_noisy
        fitness_evaluations_actual += 1

        n_iters += 1
        assert fitness_evaluations == fitness_evaluations_actual

    return n_iters, fitness_evaluations


def ollga(n, lam, q, f, k, p, c, filename):
    def algo_fun(n, lam, q, f, k, p, c, x):
        m_0, m_1, fitness_evaluations_1, x_mutated = quick_ollga_mutation(n, lam, q, f, k, p, x)
        y, fy_noisy, fitness_evaluations_2 = crossover(n, lam, q, f, k, c, x, m_0, m_1, x_mutated)
        return y, fy_noisy, fitness_evaluations_1 + fitness_evaluations_2

    return algorithm(n, lam, q, algo_fun, f, k, p, c, 2 * lam + 1, filename)


def lea(n, lam, q, f, k, p, c, filename):
    def algo_fun(n, lam, q, f, k, p, c, x):
        x_mutated, fx_noisy, fitness_evaluations = quick_lea_mutation(n, lam, q, f, k, p, x)
        return x_mutated, fx_noisy, fitness_evaluations

    return algorithm(n, lam, q, algo_fun, f, k, p, c, lam + 1, filename)


def tlea(n, lam, q, f, k, p, c, filename):
    def algo_fun(n, lam, q, f, k, p, c, x):
        x_mutated, fx_noisy, fitness_evaluations = quick_lea_mutation(n, lam, q, f, k, p, x)
        return x_mutated, fx_noisy, fitness_evaluations

    return algorithm(n, 2 * lam, q, algo_fun, f, k, p, c, 2 * lam + 1, filename)


def clea(n, lam, q, f, k, p, c, filename):
    fitness_evaluations = lam
    def algo_fun(n, lam, q, f, k, p, c, x):
        x_mutated, fx_noisy, fitness_evaluations = quick_lea_mutation(n, lam, q, f, k, p, x)
        return x_mutated, fx_noisy, fitness_evaluations
    
    n_iters = 0
    if is_quick(f):
        x = np.random.binomial(n, 1 / 2)
        assert 0 <= x <= n
    else:
        x = np.random.randint(0, 2, n)

    n_iters_max = stop_criterion(n, filename)
    while not_find_optimum(x, n, f):
        y, fy_noisy, fitness_evaluations_actual = algo_fun(n, lam, q, f, k, p, c, x)

        x = y

        n_iters += 1
        assert fitness_evaluations == fitness_evaluations_actual

    return n_iters, fitness_evaluations