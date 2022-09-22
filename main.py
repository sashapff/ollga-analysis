import argparse
import math
import random
import numpy as np
from multiprocessing import Pool
from functools import partial
import os


def option_parse(n, option):
    if option == 'logn':
        return math.log(n)
    if option == '1div6e':
        return 1 / 6 / math.e


def f(x):
    return bin(x).count('1')


def flip(x, i):
    return x ^ (2 ** i)


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
            y = flip(y, i)

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
            if x ^ (2 ** i) != x_mutated ^ (2 ** i) and np.random.uniform() < 1 / lam:
                y = flip(y, i)

        f_y = f_noisy(y, n, q)

        if f_y > f_y_crossover:
            y_crossover = y
        f_y_crossover = f_noisy(y_crossover, n, q)

    return y_crossover, f_y_crossover


def algorithm(n, lam, q, algo_fun):
    n_iters = 0
    x = random.randint(0, 2 ** n - 1)
    f_x = f_noisy(x, n, q)
    while f(x) != n and n_iters < n ** 3:
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


def thread_run(algo, n, lam, q, n_runs, thread_id):
    random.seed(thread_id)
    np.random.seed(thread_id)

    runtime_dist = []
    for _ in range(n_runs):
        runtime_dist.append(algo(n, lam, q))
    return runtime_dist


def run(algo, n, lam, q, n_threads, n_runs, file):
    with Pool(n_threads) as p:
        run_func = partial(thread_run, algo, n, lam, q, n_runs)
        runtime_dist = np.array(p.map(run_func, range(n_threads))).flatten()

        for n_iters in runtime_dist:
            file.write(f'{n_iters}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--algo', type=str)
    parser.add_argument('--n_deg', type=int)
    parser.add_argument('--lam', type=str)
    parser.add_argument('--q', type=str)
    parser.add_argument('--threads', type=int)
    parser.add_argument('--runs', type=int)
    args = parser.parse_args()

    algo = args.algo
    n = 2 ** args.n_deg
    lam = int(option_parse(n, args.lam))
    q = option_parse(n, args.q)
    n_threads = args.threads
    n_runs = args.runs

    algo_dict = {
        'ollga': ollga,
        'oplea': oplea
    }

    data_path = 'data/'
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    with open(data_path + f'{algo}: n_deg={args.n_deg}, lam={args.lam}, q={args.q}.txt', 'w') as file:
        run(algo_dict[algo], n, lam, q, n_threads, n_runs, file)
