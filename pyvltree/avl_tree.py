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

    def size(self):
        return self._root.size() if self._root is not None else 0

    def insert(self, obj):
        """ Insert an element into the tree.

            If an element equal (by the obj's __eq__ method) to obj is
            inserted, it will not be added.
        """

        if self._root is None:
            self._root = _Node(obj)
        else:
            self._root.insert(obj)

    def delete(self, obj):
        """ """

        if self._root is None:
            return

        to_delete = self._root.find(obj)

        if to_delete is None:
            return

        if to_delete.has_two_children():
            pass
        elif to_delete.has_left_child():
            if to_delete.is_root():
                self._root = to_delete.left
            elif to_delete.is_left_child():
                to_delete.parent.left = to_delete.left
            elif to_delete.is_right_child():
                to_delete.parent.right = to_delete.left

            to_delete.left.parent = to_delete.parent

        elif to_delete.has_right_child():
            if to_delete.is_root():
                self._root = to_delete.right
            elif to_delete.is_left_child():
                to_delete.parent.left = to_delete.right
            elif to_delete.is_right_child():
                to_delete.parent.right = to_delete.right

            to_delete.right.parent = to_delete.parent
        else:
            if to_delete.is_root():
                self._root = None
            elif to_delete.is_left_child():
                to_delete.parent.left = None
            elif to_delete.is_right_child():
                to_delete.parent.right = None

    def print(self):
        self._root.print() if self._root is not None else print(self._root)
