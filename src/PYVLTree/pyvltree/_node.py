class _Node:
    """ """

    def __init__(self, obj, parent=None):
        self.obj = obj
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, obj):
        """ """

        if obj == self.obj:
            return self
        elif obj < self.obj:
            return self.left.find(obj) if self.left is not None else None
        else:
            return self.right.find(obj) if self.right is not None else None

    def insert(self, obj):
        """ """

        if obj <= self.obj:
          if self.left is None:
                self.left = _Node(obj, self)
            else:
                self.left.insert(obj)
        else:
            if self.right is None:
                self.right = _Node(obj, self)
            else:
                self.right.insert(obj)

    def delete(self):
        if self.is_left_child():
            self.parent.left = None
        elif self.is_right_child():
            self.parent.right = None

    def replace(self, other):
        other.obj = self.obj

        if self.has_right_child():
            if self.is_left_child():
                self.parent.left = self.right
            elif self.is_right_child():
                self.parent.right = self.right

        self.delete()

    def min(self):
        if self.has_left_child():
            return self.left.min()
        else:
            return self

    def print(self):
        print((f'obj = {self.obj}, left = {self.left}, right = '
               f'{self.right}, parent = {self.parent}\n'))

        if self.has_left_child():
            self.left.print()

        if self.has_right_child():
            self.right.print()

    def is_left_child(self):
        return (self.parent.left is self
                if self.parent is not None
                else False)

    def is_right_child(self):
        return (self.parent.right is self
                if self.parent is not None
                else False)

    def has_two_children(self):
        return self.has_left_child() and self.has_right_child

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None
