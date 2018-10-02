class _AVLNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def search(self, key):

        if key == self.value:
            return self
        elif key < self.value:
            return self.left.search(key) if self._has_left_child() else None
        else:
            return self.right.search(key) if self._has_right_child() else None

    def size(self):

        if self._has_two_children():
            return 1 + self.left.size() + self.right.size()
        elif self._has_left_child():
            return 1 + self.left.size()
        elif self._has_right_child():
            return 1 + self.right.size()
        else:
            return 1

    def insert(self, value):

        if value == self.value:
            return
        elif value < self.value:
            if self.left is None:
                self.left = _AVLNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = _AVLNode(value)
            else:
                self.right.insert(value)

    def delete(self, value):

        if value < self.value:
            self.left = (self.left.delete(value)
                         if self.left is not None
                         else None)

            return self
        elif value > self.value:
            self.right = (self.right.delete(value)
                          if self.right is not None
                          else None)

            return self
        else:
            if self._has_two_children():
                self.value = self.right._min().value
                self.right.delete(self.value)

                return self
            else:
                return self.left if self.left is not None else self.right

    def _min(self):
        if self._has_left_child():
            return self.left._min()
        else:
            return self

    def _has_two_children(self):
        return self._has_left_child() and self._has_right_child()

    def _has_left_child(self):
        return self.left is not None

    def _has_right_child(self):
        return self.right is not None
