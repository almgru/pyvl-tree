from ._node import _Node


class AVLTree:
    """ """

    def __init__(self):
        self._root = None

    def find(self, obj):
        """ """

        if self._root is None:
            return None
        else:
            node = self._root.find(obj)
            return node.obj if node is not None else None

    def insert(self, obj):
        """ """

        if self._root is None:
            self._root = _Node(obj)
        else:
            self._root.insert(obj)

    def delete(self, obj):
        """ """

        if self._root is None:
            return

        to_delete = self._root.find(obj)
        replacement = None

        if to_delete is None:
            return

        if to_delete.has_two_children():
            replacement = to_delete.right.min()
        elif to_delete.has_left_child():
            replacement = to_delete.left
        elif to_delete.has_right_child():
            replacement = to_delete.right
        else:
            to_delete.delete()

        if replacement is not None:
            to_delete.replace(replacement)

        if to_delete is self._root:
            self._root = replacement

    def print(self):
        self._root.print() if self._root is not None else print(self._root)
