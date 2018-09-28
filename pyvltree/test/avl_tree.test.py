import unittest
from pyvltree.avl_tree import AVLTree


class AVLTreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()

    def insert_shall_insert_element_when_empty_tree(self):
        expected = 1

        self.tree.insert(expected)
        actual = self.tree.find(expected)

        self.assertEqual(actual, expected)

    def insert_shall_insert_element_when_tree_not_empty(self):
        first_element = "Abc"
        expected = "Def"

        self.tree.insert(first_element)
        self.tree.insert(expected)

        actual = self.tree.find(expected)

        self.assertEqual(actual, expected)
