import os
from functools import partial
from multiprocessing import Pool

import numpy as np

from tools import args_parse


def run_algorithm(algo, n, lam, q, n_runs, thread_id):
    np.random.seed(thread_id)

    runtime_dist = []
    n_failed = 0
    for _ in range(n_runs):
        n_iters = algo(n, lam, q)
        runtime_dist.append(n_iters)

        if n_iters == n ** 3:
            n_failed += 1

        if n_failed >= 0.1 * n_runs:
            break
    return runtime_dist


def run(algo, n, lam, q, n_threads, n_runs, file):
    with Pool(n_threads) as p:
        run_func = partial(run_algorithm, algo, n, lam, q, n_runs)
        runtime_dist = p.map(run_func, range(n_threads))

        for dist in runtime_dist:
            for n_iters in dist:
                file.write(f'{n_iters}\n')


if __name__ == '__main__':
    algo_name, algo, n_deg, n, lam_name, lam, q_name, q, n_threads, n_runs, data_path, plots_data = args_parse()

    if not os.path.exists(data_path):
        os.mkdir(data_path)

    with open(data_path + f'{algo_name}: n_deg={n_deg}, lam={lam_name}, q={q_name}.txt', 'w') as file:
        run(algo, n, lam, q, n_threads, n_runs, file)
