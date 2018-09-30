from ._avl_node import _AVLNode


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
            self._root = _AVLNode(obj)
        else:
            self._root.insert(obj)

    def delete(self, obj):
        """ """

        self._root = (self._root.delete(obj)
                      if self._root is not None
                      else none)

    def print(self):
        self._root.print() if self._root is not None else print(self._root)
