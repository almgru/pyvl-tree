from ._avl_node import _AVLNode


class AVLTree():
    """ """

    def __init__(self):
        self._root = None

    def find(self, value):
        """ """

        node = self._root.find(value) if self._root is not None else None

        return node.value if node is not None else None

    def size(self):
        return self._root.size() if self._root is not None else 0

    def insert(self, value):
        """ Insert an element into the tree.

            If an element equal (by the obj's __eq__ method) to obj is
            inserted, it will not be added.
        """

        if self._root is None:
            self._root = _AVLNode(value)
        else:
            self._root.insert(value)

    def delete(self, value):
        """ """

        self._root = (self._root.delete(value)
                      if self._root is not None
                      else none)
