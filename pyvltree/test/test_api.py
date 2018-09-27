import unittest
import random
from datetime import datetime
from pyvltree.avl_tree import AVLTree


class APITest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        random.seed(datetime.now())

    def setUp(self):
        self.tree = AVLTree()

    def test_tree_shall_contain_equivalent_element_after_insert(self):
        ITERATIONS = 1000

        for i in range(ITERATIONS):
            element = random.randrange(100)
            self.tree.insert(element)
            foundElement = self.tree.find(element)
            self.assertEqual(element, foundElement)
