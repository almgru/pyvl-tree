#!/usr/bin/env python

import sys
import pandas
import matplotlib

matplotlib.use('agg')

import matplotlib.pyplot as plt


def main(argv):
    data = pandas.read_table('data.txt', delim_whitespace=True,
                             names=('n', 't_s', 't_i', 't_d'))
    plot_linear(data)
    plot_log(data)


def plot_linear(data):
    subset = data.tail(20)

    plt.plot(subset.n, subset.t_d, label='Delete')
    plt.plot(subset.n, subset.t_i, label='Insert')
    plt.plot(subset.n, subset.t_s, label='Search')

    plt.xlabel('n')
    plt.ylabel('time / operation (μs)')

    plt.legend()

    plt.savefig('plot-linear.png')
    plt.gcf().clear()


def plot_log(data):
    plt.semilogx(data.n, data.t_d, label='Delete', basex=2)
    plt.semilogx(data.n, data.t_i, label='Insert', basex=2)
    plt.semilogx(data.n, data.t_s, label='Search', basex=2)

    plt.xlabel('n')
    plt.ylabel('time / operation (μs)')

    plt.legend()

    plt.savefig('plot-log.png')
    plt.gcf().clear()


if __name__ == '__main__':
    main(sys.argv)
