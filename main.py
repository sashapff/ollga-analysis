import random
import numpy as np
from multiprocessing import Pool
from functools import partial
import os
from tools import args_parse


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
    algo_name, algo, n_deg, n, lam_name, lam, q_name, q, n_threads, n_runs = args_parse()

    data_path = 'data/'
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    with open(data_path + f'{algo_name}: n_deg={n_deg}, lam={lam_name}, q={q_name}.txt', 'w') as file:
        run(algo, n, lam, q, n_threads, n_runs, file)
