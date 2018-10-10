#!/usr/bin/env python3

import time
import random
import argparse
import gc
import sys
from datetime import datetime

from pyvltree.avl_tree import AVLTree

random.seed(datetime.now())

parser = argparse.ArgumentParser()
parser.add_argument('n', help='Number of operations to perform.', type=int)
parser.add_argument('-i', '--iterations',
                    help='Iterations to perform when n reached.', type=int)
args = parser.parse_args()

n = args.n

tree = AVLTree()
gc.disable()
sample = random.sample(range(-n, n), n)

for i, val in enumerate(sample):
    if n // 10 != 0 and i % (n // 10) == 0:
        sys.stdout.write(".")
        sys.stdout.flush()
    tree.insert(val)

print()

if args.iterations:
    search_total = 0
    insert_total = 0
    delete_total = 0

    for i in range(args.iterations):
        to_search = random.randrange(-n, n)
        to_insert = random.randrange(-n, n)
        to_delete = random.randrange(-n, n)

        start = time.perf_counter()
        tree.search(to_search)
        search_total += time.perf_counter() - start

        start = time.perf_counter()
        tree.insert(to_insert)
        insert_total += time.perf_counter() - start

        tree.delete(to_insert)

        start = time.perf_counter()
        tree.delete(to_delete)
        delete_total += time.perf_counter() - start

        tree.insert(to_delete)

print("{0}\t{1}\t{2}\t{3}\n".format(n, search_total / args.iterations,
                                    insert_total / args.iterations,
                                    delete_total / args.iterations))
