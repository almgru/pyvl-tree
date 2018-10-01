import unittest
from pyvltree.avl_tree import AVLTree
from pyvltree._avl_node import _AVLNode


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

    def test_delete__set_root_to_none__deleting_leaf_root(self):
        self.tree._root = _AVLNode(1)
        self.tree.delete(1)

        self.assertTrue(self.tree._root is None)

    def test_delete__update_root__deleting_root_with_children(self):
        self.tree._root = _AVLNode(5)
        self.tree._root.left = _AVLNode(2)
        self.tree._root.right = _AVLNode(7)

        self.tree.delete(5)

        self.assertEqual(self.tree._root.value, 7)

    def test_delete__correct_state__deleting_leaf_node(self):
        self.tree._root = _AVLNode(10)
        self.tree._root.left = _AVLNode(5)

        self.tree.delete(5)

        self.assertEqual(self.tree._root.value, 10)
        self.assertTrue(self.tree._root.right is None)

    def test_delete__correct_state__deleting_node_with_one_child(self):
        self.tree._root = _AVLNode(20)
        self.tree._root.right = _AVLNode(50)
        self.tree._root.right.left = _AVLNode(30)

        self.tree.delete(50)

        self.assertEqual(self.tree._root.value, 20)
        self.assertEqual(self.tree._root.right.value, 30)
        self.assertTrue(self.tree._root.right.left is None)

    def test_delete__correct_state__deleting_node_with_two_children(self):
        self.tree._root = _AVLNode(100)
        self.tree._root.left = _AVLNode(50)
        self.tree._root.left.left = _AVLNode(25)
        self.tree._root.left.right = _AVLNode(75)

        self.tree.delete(50)

        self.assertEqual(self.tree._root.value, 100)
        self.assertEqual(self.tree._root.left.value, 75)
        self.assertEqual(self.tree._root.left.left.value, 25)
