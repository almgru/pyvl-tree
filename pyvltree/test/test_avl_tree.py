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
        expected = 3

        self.tree.insert(5)
        self.tree.insert(expected)

        actual = self.tree._root.left.value

        self.assertEqual(actual, expected)

    def test_insert__correct_position__inserted_less_than_root(self):
        expected = 1

        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(3)

        self.tree.insert(expected)

        actual = (self.tree._root.left.left.value
                  if self.tree._root.left.left is not None
                  else None)

        self.assertEqual(actual, expected)

    def test_insert__correct_position__inserted_greater_than_root(self):
        expected = 4

        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)

        self.tree.insert(expected)

        actual = (self.tree._root.right.right.value
                  if self.tree._root.right.right is not None
                  else None)

        self.assertEqual(actual, expected)

    def test_insert__not_insert_element__tree_has_equivalent_element(self):
        self.tree.insert(10)

        self.tree.insert(10)

        self.assertTrue(self.tree._root.left is None)
        self.assertTrue(self.tree._root.right is None)

    def test_insert__rebalance__right_child_and_right_heavy(self):
        self.tree.insert(1)
        self.tree.insert(2)

        self.tree.insert(3)

        self.assertEqual(self.tree._root.value, 2)
        self.assertEqual(self.tree._root.left.value, 1)
        self.assertEqual(self.tree._root.right.value, 3)

    def test_insert__rebalance__pivot_left_child_and_left_heavy(self):
        self.tree.insert(3)
        self.tree.insert(2)

        self.tree.insert(1)

        self.assertEqual(self.tree._root.value, 2)
        self.assertEqual(self.tree._root.left.value, 1)
        self.assertEqual(self.tree._root.right.value, 3)

    def test_insert__rebalance__left_child_and_right_heavy(self):
        self.tree.insert(3)
        self.tree.insert(1)

        self.tree.insert(2)

        self.assertEqual(self.tree._root.value, 2)
        self.assertEqual(self.tree._root.left.value, 1)
        self.assertEqual(self.tree._root.right.value, 3)

    def test_insert__rebalance__right_child_and_left_heavy(self):
        self.tree.insert(1)
        self.tree.insert(3)

        self.tree.insert(2)

        self.assertEqual(self.tree._root.value, 2)
        self.assertEqual(self.tree._root.left.value, 1)
        self.assertEqual(self.tree._root.right.value, 3)

    def test_insert__rebalance__pivot_has_two_children(self):
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(7)
        self.tree.insert(6)
        self.tree.insert(8)

        self.tree.insert(9)

        self.assertEqual(self.tree._root.value, 7)
        self.assertEqual(self.tree._root.left.value, 5)
        self.assertEqual(self.tree._root.right.value, 8)
        self.assertEqual(self.tree._root.left.left.value, 4)
        self.assertEqual(self.tree._root.left.right.value, 6)
        self.assertEqual(self.tree._root.right.right.value, 9)

    def test_insert__rebalance__testetset(self):
        self.tree.insert(37)
        self.tree.insert(7)
        self.tree.insert(75)
        self.tree.insert(45)
        self.tree.insert(20)
        self.tree.insert(54)
        self.tree.insert(59)

        self.tree.delete(37)

        self.assertEqual(self.tree._root.value, 45)
        self.assertEqual(self.tree._root.left.value, 7)
        self.assertEqual(self.tree._root.left.right.value, 20)
        self.assertEqual(self.tree._root.right.value, 59)
        self.assertEqual(self.tree._root.right.left.value, 54)
        self.assertEqual(self.tree._root.right.right.value, 75)

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
        self.tree.insert(100)
        self.tree.insert(125)
        self.tree.insert(50)
        self.tree.insert(25)
        self.tree.insert(75)

        self.tree.delete(50)

        self.assertEqual(self.tree._root.value, 100)
        self.assertEqual(self.tree._root.left.value, 75)
        self.assertEqual(self.tree._root.right.value, 125)
        self.assertEqual(self.tree._root.left.left.value, 25)

    def test_delete__rebalance__pivot_right_child_and_right_heavy(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(4)

        self.tree.delete(1)

        self.assertEqual(self.tree._root.value, 3)
        self.assertEqual(self.tree._root.left.value, 2)
        self.assertEqual(self.tree._root.right.value, 4)

    def test_delete__rebalance__pivot_left_child_and_left_heavy(self):
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(1)

        self.tree.delete(4)

        self.assertEqual(self.tree._root.value, 2)
        self.assertEqual(self.tree._root.left.value, 1)
        self.assertEqual(self.tree._root.right.value, 3)

    def test_delete__rebalance__pivot_right_child_and_left_heavy(self):
        self.tree.insert(2)
        self.tree.insert(1)
        self.tree.insert(4)
        self.tree.insert(3)

        self.tree.delete(1)

        self.assertEqual(self.tree._root.value, 3)
        self.assertEqual(self.tree._root.left.value, 2)
        self.assertEqual(self.tree._root.right.value, 4)

    def test_delete__rebalance__pivot_left_child_and_right_heavy(self):
        self.tree.insert(3)
        self.tree.insert(1)
        self.tree.insert(4)
        self.tree.insert(2)

        self.tree.delete(4)

        self.assertEqual(self.tree._root.value, 2)
        self.assertEqual(self.tree._root.left.value, 1)
        self.assertEqual(self.tree._root.right.value, 3)

    def test_delete__rebalance__pivot_has_two_children(self):
        self.tree.insert(3)
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(1)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(7)

        self.tree.delete(1)

        self.assertEqual(self.tree._root.value, 5)
        self.assertEqual(self.tree._root.left.value, 3)
        self.assertEqual(self.tree._root.left.left.value, 2)
        self.assertEqual(self.tree._root.left.right.value, 4)
        self.assertEqual(self.tree._root.right.value, 6)
        self.assertEqual(self.tree._root.right.right.value, 7)

    def test_search__find_element__element_is_at_root(self):
        expected = 1
        self.tree._root = Helper.create_node(expected)

        actual = self.tree.search(expected)

        self.assertEqual(actual, expected)

    def test_search__find_element__element_is_not_at_root(self):
        expected = 4
        self.tree._root = Helper.create_node(3)
        self.tree._root.right = Helper.create_node(expected)

        actual = self.tree.search(expected)

        self.assertEqual(actual, expected)

    def test_search__return_None__tree_is_empty(self):
        actual = self.tree.search(3)

        self.assertTrue(actual is None)

    def test_search__return_None__element_not_in_tree(self):
        self.tree._root = Helper.create_node(10)
        self.tree._root.right = Helper.create_node(15)

        actual = self.tree.search(5)

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
        self.tree.insert(4)
        self.tree.insert(2)
        self.tree.insert(6)

        actual = self.tree.size()

        self.assertEqual(actual, expected)

    def test_size__expected__tree_has_nodes_with_one_child(self):
        expected = 3
        self.tree.insert(10)
        self.tree.insert(5)
        self.tree.insert(7)

        actual = self.tree.size()

        self.assertEqual(actual, expected)
