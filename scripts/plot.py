#!/usr/bin/env python

import sys
import argparse
import pandas
import matplotlib

matplotlib.use('agg')

import matplotlib.pyplot as plt


def main(argv):
    args = init_argparse().parse_args()
    data = pandas.read_table(args.input_file, delim_whitespace=True,
                             names=('n', 't_s', 't_i', 't_d'))
    out = args.out_dir if args.out_dir else ""

    if out != "" and not out.endswith("/"):
        out += '/'

    plot_linear(data, out)
    plot_log(data, out)


def plot_linear(data, out):
    subset = data.tail(20)

    plt.plot(subset.n, subset.t_d, label='Delete')
    plt.plot(subset.n, subset.t_i, label='Insert')
    plt.plot(subset.n, subset.t_s, label='Search')

    plt.xlabel('n')
    plt.ylabel('time / operation (μs)')

    plt.legend()

    plt.savefig(out + 'plot-linear.png')
    plt.gcf().clear()


def plot_log(data, out):
    plt.semilogx(data.n, data.t_d, label='Delete', basex=2)
    plt.semilogx(data.n, data.t_i, label='Insert', basex=2)
    plt.semilogx(data.n, data.t_s, label='Search', basex=2)

    plt.xlabel('n')
    plt.ylabel('time / operation (μs)')

    plt.legend()

    plt.savefig(out + 'plot-log.png')
    plt.gcf().clear()

def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', 
                        help="Text file with data to generate plot from.")
    parser.add_argument('-o', '--out-dir',
                        help="Optional relative path to save plots to.")
    return parser


if __name__ == '__main__':
    main(sys.argv)
