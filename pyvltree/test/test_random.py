import unittest
import random
from datetime import datetime

from .helper import Helper
from pyvltree.avl_tree import AVLTree


class TestRandom(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()
        random.seed(datetime.now())

    def test_height__be_less_than_max_height__inserting_n_elements(self):
        n = 16384
        expected_max_height = Helper.get_expected_max_height(n)

        for val in random.sample(range(-n * 2, n * 2), n):
            self.tree.insert(val)

        actual = Helper.find_tree_height(self.tree._root)

        self.assertTrue(actual <= expected_max_height)

    def test_search__find_all_elements__random_insertions_and_deletions(self):
        to_insert = set(random.sample(range(-10_000, 10_000), 1024))
        to_delete = set(random.sample(to_insert, 512))
        expected = set(to_insert).difference(to_delete)

        for val in to_insert:
            self.tree.insert(val)

        for val in to_delete:
            self.tree.delete(val)

        for val in expected:
            self.assertEqual(self.tree.search(val), val)

    def test_size__correct__random_insertions_and_deletions(self):
        insertions = 1024
        deletions = 512
        to_insert = set(random.sample(range(-10_000, 10_000), insertions))
        to_delete = set(random.sample(to_insert, deletions))
        expected = insertions - deletions

        for val in to_insert:
            self.tree.insert(val)

        for val in to_delete:
            self.tree.delete(val)

        actual = self.tree.size()
        self.assertEqual(actual, expected)
