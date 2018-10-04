import unittest
import random
from datetime import datetime

from .helper import Helper
from pyvltree.avl_tree import AVLTree


class TestRandom(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()
        random.seed(datetime.now())

    def test_height__should_be_log1024__inserting_1024_elements(self):
        expected_min = 9
        expected_max = 11

        for val in random.sample(range(-100_000, 100_000), 1024):
            self.tree.insert(val)

        actual = Helper.find_tree_height(self.tree._root)

        self.assertTrue(expected_min <= actual <= expected_max)

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
