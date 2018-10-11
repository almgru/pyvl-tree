#!/usr/bin/env python

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_table('data.txt', delim_whitespace=True,
                     names=('n', 't_s', 't_i', 't_d'))

plt.semilogx(data.n, data.t_s, label='Search', basex=2)
plt.semilogx(data.n, data.t_i, label='Insert', basex=2)
plt.semilogx(data.n, data.t_d, label='Delete', basex=2)

plt.xlabel('n')
plt.ylabel('time / operation (μs)')

plt.legend()

plt.savefig('plot.png')
