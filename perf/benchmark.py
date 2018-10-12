#!/usr/bin/env python3

from datetime import datetime
import time
import random
import sys
import gc
import argparse
import numpy

from pyvltree.avl_tree import AVLTree


def main(argv):
    gc.disable()
    random.seed(datetime.now())

    args = init_argparse().parse_args()

    tree = populate_tree(-args.n, args.n, args.n)

    search_times = []
    insert_times = []
    delete_times = []

    iterate(tree, args, search_times, insert_times, delete_times)

    mean_search = numpy.mean(search_times)
    mean_insert = numpy.mean(insert_times)
    mean_delete = numpy.mean(delete_times)

    print("{0}\t{1}\t{2}\t{3}".format(args.n, mean_search * 1e6,
                                      mean_insert * 1e6, mean_delete * 1e6))


def populate_tree(min_, max_, n):
    tree = AVLTree()
    sample = random.sample(range(min_, max_), n)

    for val in sample:
        tree.insert(val)

    return tree


def iterate(tree, args, search_arr, ins_arr, del_arr):
    def _time_call(fun, *args):
        start = time.perf_counter()
        fun(*args)
        return time.perf_counter() - start

    for i in range(args.i):
        to_search = random.randrange(-args.n, args.n)
        to_insert = random.randrange(-args.n, args.n)
        to_delete = random.randrange(-args.n, args.n)

        search_arr.append(_time_call(tree.search, to_search))

        exists = tree.search(to_insert) == to_insert
        ins_arr.append(_time_call(tree.insert, to_insert))
        if not exists:
            tree.delete(to_insert)

        exists = tree.search(to_delete) == to_delete
        del_arr.append(_time_call(tree.delete, to_delete))
        if exists:
            tree.insert(to_delete)


def init_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', help='Number of operations to perform.', type=int)
    parser.add_argument('i', help='Iterations to perform when n reached.',
                        type=int)
    return parser


if __name__ == '__main__':
    main(sys.argv)
