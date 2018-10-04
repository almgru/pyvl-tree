import math

from pyvltree._avl_node import _AVLNode


class Helper:

    @staticmethod
    def create_node(value):
        return _AVLNode(value)

    @staticmethod
    def find_tree_height(node):
        if node is None:
            return -1

        if node.left is not None and node.right is not None:
            return (1 + max(Helper.find_tree_height(node.left),
                    Helper.find_tree_height(node.right)))
        elif node.left is not None:
            return 1 + Helper.find_tree_height(node.left)
        elif node.right is not None:
            return 1 + Helper.find_tree_height(node.right)
        else:
            return 0

    @staticmethod
    def get_expected_max_height(n):
        # See en.wikipedia.org/wiki/AVL_Tree#Comparison_to_other_structures
        phi = (1 + math.sqrt(5)) / 2
        c = 1 / math.log(phi, 2)
        b = (c / 2) * math.log(5, 2) - 2
        d = 1 + 1 / (math.pow(phi, 4) * math.sqrt(5))

        return c * math.log(n + d, 2) + b
