class _AVLNode:
    """ """

    def __init__(self, obj):
        self.obj = obj
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

    def size(self):
        """ Time complexity: O(n) """

        if self.has_two_children():
            return self.left.size() + self.right.size()
        elif self.has_left_child():
            return self.left.size()
        elif self.has_right_child():
            return self.right.size()
        else:
            return 1

    def insert(self, obj):
        """ """

        if obj == self.obj:
            return
        elif obj < self.obj:
            if self.left is None:
                self.left = _AVLNode(obj)
            else:
                self.left.insert(obj)
        else:
            if self.right is None:
                self.right = _AVLNode(obj)
            else:
                self.right.insert(obj)

    def delete(self, obj):
        """ """
        new_sub_root = None

        if obj < self.obj:
            self.left = (self.left.delete(obj) 
                         if self.left is not None
                         else None)
            new_sub_root = self
        elif obj > self.obj:
            self.right = (self.right.delete(obj) 
                          if self.right is not None
                          else None)
            new_sub_root = self
        else:
            if self.has_two_children():
                self.obj = self.right.min().obj
                self.right.delete(self.obj)
                new_sub_root = self
            else:
                new_sub_root = (self.left 
                                if self.left is not None 
                                else self.right)

        return new_sub_root

    def min(self):
        if self.has_left_child():
            return self.left.min()
        else:
            return self

    def has_two_children(self):
        return self.has_left_child() and self.has_right_child()

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def is_leaf(self):
        return not self.has_left_child() and not self.has_right_child()
