from ._avl_node import _AVLNode


class AVLTree():
    """ A recursive implementation of a self-balancing binary search tree.
        Self-balancing is achieved using the AVL algorithms.
    """

    def __init__(self):
        self._root = None

    def search(self, key):
        """ Search for an element given an equivalent key.

            Equivalence is determined from the element's __eq__ method.

            Average time complexity: O(log n)
            Worst-case time complexity: O(n)

            Returns the element equivalent to the key if found, None otherwise.
        """

        node = self._root.search(key) if self._root is not None else None

        return node.value if node is not None else None

    def size(self):
        """ Calculates the number of elements in the tree.

            Time complexity: O(n)

            Returns the number of elements in the tree.
        """

        return self._root.size() if self._root is not None else 0

    def insert(self, value):
        """ Insert an element into the tree.

            Duplicate elements will be silently discarded.

            Average time complexity: O(log n)
            Worst-case time complexity: O(n)
        """

        self._root = (_AVLNode(value) 
                      if self._root is None 
                      else self._root.insert(value))

    def delete(self, value):
        """ Deletes an element from the tree.

            If the element deleted had two children, it will be replaced by
            its in-order successor.

            Average time complexity: O(log n)
            Worst-case time complexity: O(n)
        """

        self._root = (self._root.delete(value)
                      if self._root is not None
                      else None)
