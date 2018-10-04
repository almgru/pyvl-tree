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
