import os
from functools import partial
from multiprocessing import Pool

import numpy as np

from tools import args_parse
from algorithms import stop_criterion


def run_algorithm(algo, n, lam, q, f, k, p, c, n_runs, thread_id):
    np.random.seed(thread_id)

    runtime_dist = []
    n_failed = 0
    for _ in range(n_runs):
        n_iters, fitness_evaluations = algo(n, lam, q, f, k, p, c)

        if n_iters == stop_criterion(n):
            n_failed += 1
            n_iters = -1

        runtime_dist.append(n_iters * fitness_evaluations)

    return runtime_dist


def run(algo, n, lam, q, f, k, p, c, n_threads, n_runs, file):
    with Pool(n_threads) as pool:
        run_func = partial(run_algorithm, algo, n, lam, q, f, k, p, c, n_runs)
        runtime_dist = pool.map(run_func, range(n_threads))

        for dist in runtime_dist:
            for n_iters in dist:
                file.write(f'{n_iters}\n')


if __name__ == '__main__':
    algo_name, algo, n_deg, n, lam_name, lam, q_name, q, f, fitness_name, k, p, c, n_threads, n_runs, data_path, \
    plots_data = args_parse()

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    with open(data_path + f'{algo_name}: n_deg={n_deg}, lam={lam_name}, q={q_name}.txt', 'w') as file:
        run(algo, n, lam, q, f, k, p, c, n_threads, n_runs, file)
