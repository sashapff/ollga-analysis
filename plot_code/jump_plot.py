import os

import numpy as np

from tools import option_parse, option_tex_parse


def plot(algo_name, lam_name, q_name, data_path, n_deg_from, n_deg_to):
    latex_output = ''
    algo_latex_code = '\ollga' if algo_name == 'ollga' else ('\oplea' if lam_name != '1' else '\oea')
    lam_tex = option_tex_parse(lam_name)
    latex_output += '\t\t\\addplot plot [error bars/.cd, y dir=both, y explicit] coordinates\n'
    latex_output += '\t\t{'
    for n_deg in range(n_deg_from, n_deg_to + 1):
        file_name = data_path + f'{algo_name}: n_deg={n_deg}, lam={lam_name}, q={q_name}.txt'
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            data = np.loadtxt(file_name)
            n = 1 << n_deg
            lam = option_parse(n, lam_name, k=3)
            data = data[data >= 0]
            n_iters = data.mean()
            std = data.std()

            latex_output += f'({n},{n_iters})+-(0,{std})'

    latex_output += '};\n'
    latex_output += '\t\t' + (
        '% ' if q_name != '0' else '') + '\\addlegendentry{' + algo_latex_code + (
                        (', $\\lambda=' + lam_tex[1:-1] + '$') if lam_name != 1 else '') + '};\n'

    return latex_output


if __name__ == '__main__':
    algo_name_1 = 'ollga'
    algo_name_2 = 'lea'
    algo_name_3 = 'oea'
    plots_path = '../plots/jump/'
    latex_plots_path = '../latex_plots/jump/'
    data_path = '../data/jump/k=3/'

    n_deg_from, n_deg_to = 3, 7

    if not os.path.exists(plots_path):
        os.makedirs(plots_path)

    if not os.path.exists(latex_plots_path):
        os.makedirs(latex_plots_path)

    for q_name in ['0', 'logn_div_n', '1_div_6e']:
        q_tex = option_tex_parse(q_name)
        name = f'q={q_name}'

        latex_output_1 = plot('ollga', 'sqrtn_pow_k_minus_1_div_sqrt_k_pow_k', q_name, data_path, n_deg_from, n_deg_to)
        latex_output_2 = plot('ollga', 'logn', q_name, data_path, n_deg_from, n_deg_to)
        latex_output_3 = plot('lea', 'sqrtn_pow_k_minus_1_div_sqrt_k_pow_k', q_name, data_path, n_deg_from, n_deg_to)
        latex_output_4 = plot('lea', 'logn', q_name, data_path, n_deg_from, n_deg_to)
        latex_output_5 = plot('lea', '1', q_name, data_path, n_deg_from, n_deg_to)

        with open(latex_plots_path + name + '.tex', 'w') as file:
            file.write(latex_output_1)
            file.write(latex_output_2)
            file.write(latex_output_5)
            file.write(latex_output_3)
            file.write(latex_output_4)
