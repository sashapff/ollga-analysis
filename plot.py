import os

import matplotlib.pyplot as plt
import numpy as np

from tools import plots_args_parse, data_path, plots_path


def plot(algo_name, n_deg_from, n_deg_to, lam_name, q_name, label, color):
    keys = []
    values = []

    for n_deg in range(n_deg_from, n_deg_to + 1):
        file_name = data_path + f'{algo_name}: n_deg={n_deg}, lam={lam_name}, q={q_name}.txt'
        data = np.loadtxt(file_name)
        n = 1 << n_deg
        n_iters = data.mean()
        keys.append(n)
        values.append(n_iters)

        plt.errorbar(n, n_iters, yerr=data.std(), color=color, capsize=3)

    plt.plot(keys, values, label=label, color=color)


if __name__ == '__main__':
    algo_name_1, algo_tex_1, algo_name_2, algo_tex_2, n_deg_from, n_deg_to, lam_name, lam_tex, q_name, q_tex, y_scale \
        = plots_args_parse()

    if not os.path.exists(plots_path):
        os.mkdir(plots_path)

    plt.title(f'$\lambda$={lam_tex}, q={q_tex}')

    plot(algo_name_1, n_deg_from, n_deg_to, lam_name, q_name, algo_tex_1, 'black')
    plot(algo_name_2, n_deg_from, n_deg_to, lam_name, q_name, algo_tex_2, 'tab:red')

    plt.legend()
    plt.xlabel('number of individuals')
    plt.ylabel('number of iterations to find the optimum')
    plt.yscale(y_scale)

    plt.savefig(plots_path + f'{algo_name_1}_{algo_name_2}: lam={lam_name}, q={q_name}.png')
