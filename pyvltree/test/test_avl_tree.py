import unittest
from .helper import Helper
from pyvltree.avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()

    def test_insert__insert_element__empty_tree(self):
        expected = 1

        self.tree.insert(expected)
        actual = self.tree._root.value

        self.assertEqual(actual, expected)

    def test_insert__insert_element__tree_not_empty(self):
        first_element = 5
        expected = 3

        self.tree.insert(first_element)
        self.tree.insert(expected)

        actual = self.tree._root.left.value

        self.assertEqual(actual, expected)

    def test_insert__not_insert_element__tree_has_equivalent_element(self):
        self.tree._root = Helper.create_node(10)
        
        self.tree.insert(10)

        self.assertTrue(self.tree._root.left is None)
        self.assertTrue(self.tree._root.right is None)

    def test_delete__set_root_to_none__deleting_leaf_root(self):
        self.tree._root = Helper.create_node(1)
        self.tree.delete(1)

        self.assertTrue(self.tree._root is None)

    def test_delete__update_root__deleting_root_with_children(self):
        self.tree._root = Helper.create_node(5)
        self.tree._root.left = Helper.create_node(2)
        self.tree._root.right = Helper.create_node(7)

        self.tree.delete(5)

        self.assertEqual(self.tree._root.value, 7)

    def test_delete__correct_state__deleting_leaf_node(self):
        self.tree._root = Helper.create_node(10)
        self.tree._root.left = Helper.create_node(5)

        self.tree.delete(5)

        self.assertEqual(self.tree._root.value, 10)
        self.assertTrue(self.tree._root.right is None)

    def test_delete__correct_state__deleting_node_with_one_child(self):
        self.tree._root = Helper.create_node(20)
        self.tree._root.right = Helper.create_node(50)
        self.tree._root.right.left = Helper.create_node(30)

        self.tree.delete(50)

        self.assertEqual(self.tree._root.value, 20)
        self.assertEqual(self.tree._root.right.value, 30)
        self.assertTrue(self.tree._root.right.left is None)

    def test_delete__correct_state__deleting_node_with_two_children(self):
        self.tree._root = Helper.create_node(100)
        self.tree._root.left = Helper.create_node(50)
        self.tree._root.left.left = Helper.create_node(25)
        self.tree._root.left.right = Helper.create_node(75)

        self.tree.delete(50)

        self.assertEqual(self.tree._root.value, 100)
        self.assertEqual(self.tree._root.left.value, 75)
        self.assertEqual(self.tree._root.left.left.value, 25)

    def test_find__find_element__element_is_at_root(self):
        expected = 1
        self.tree._root = Helper.create_node(expected)

        actual = self.tree.find(expected)

        self.assertEqual(actual, expected)

    def test_find__find_element__element_is_not_at_root(self):
        expected = 4
        self.tree._root = Helper.create_node(3)
        self.tree._root.right = Helper.create_node(expected)

        actual = self.tree.find(expected)

        self.assertEqual(actual, expected)

    def test_find__return_None__tree_is_empty(self):
        actual = self.tree.find(3)

        self.assertTrue(actual is None)

    def test_find__return_None__element_not_in_tree(self):
        self.tree._root = Helper.create_node(10)
        self.tree._root.right = Helper.create_node(15)

        actual = self.tree.find(5)

        self.assertTrue(actual is None)

    def test_size__return_zero__tree_is_empty(self):
        expected = 0

        actual = self.tree.size()

        self.assertEqual(actual, expected)

    def test_size__return_one__tree_has_one_element(self):
        expected = 1
        self.tree._root = Helper.create_node(10)

        actual = self.tree.size()

        self.assertEqual(actual, expected)

    def test_size__expected__tree_has_node_with_two_children(self):
        expected = 3
        self.tree._root = Helper.create_node(4)
        self.tree._root.left = Helper.create_node(2)
        self.tree._root.right = Helper.create_node(6)

        actual = self.tree.size()

        self.assertEqual(actual, expected)

    def test_size__expected__tree_has_node_with_one_child(self):
        expected = 2
        self.tree._root = Helper.create_node(10)
        self.tree._root.left = Helper.create_node(5)

        actual = self.tree.size()

        self.assertEqual(actual, expected)
