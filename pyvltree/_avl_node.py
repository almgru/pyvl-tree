class _AVLNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
        self.balance_factor = 0
        self._BALANCE_THRESHOLD = 1

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
            new_height = self.height
        elif value < self.value:
            if self.left is None:
                self.left = _AVLNode(value)
                new_height = max(self.height, 1)
            else:
                self.left = self.left.insert(value)
                new_height = max(self.height, self.left.height + 1)
        else:
            if self.right is None:
                self.right = _AVLNode(value)
                new_height = max(self.height, 1)
            else:
                self.right = self.right.insert(value)
                new_height = max(self.height, self.right.height + 1)

        self.height = new_height

        self.balance_factor = self._calculate_balance_factor()

        if self._needs_rebalancing():
            new_subtree_root = self._rebalance()
        else:
            new_subtree_root = self

        return new_subtree_root

    def delete(self, value):
        if value < self.value:
            self.left = (self.left.delete(value)
                         if self.left is not None
                         else None)
            new_subtree_root = self
        elif value > self.value:
            self.right = (self.right.delete(value)
                          if self.right is not None
                          else None)
            new_subtree_root = self
        elif self._has_two_children():
            self.value = self.right._min().value
            self.right.delete(self.value)
            new_subtree_root = self
        else:
            new_subtree_root = (self.left
                                if self.left is not None
                                else self.right)

        return new_subtree_root

    def _min(self):
        if self._has_left_child():
            return self.left._min()
        else:
            return self

    def _needs_rebalancing(self):
        return abs(self.balance_factor) > self._BALANCE_THRESHOLD

    def _calculate_balance_factor(self):
        right_subtree_height = (self.right.height
                                if self._has_right_child()
                                else -1)
        left_subtree_height = (self.left.height
                               if self._has_left_child()
                               else -1)

        return right_subtree_height - left_subtree_height

    def _rebalance(self):
        if self.right is None:
            tallest_child = self.left
        elif self.left is None:
            tallest_child = self.right
        else:
            tallest_child = (self.right
                             if self.right.height > self.left.height
                             else self.left)

        if self._is_left_heavy():
            if tallest_child._is_left_heavy():  # Left-Left
                return self._rotate_right(tallest_child)
            elif tallest_child._is_right_heavy():  # Left-Right
                return (self._rotate_right(
                        tallest_child._rotate_left(tallest_child.right)))
        elif self._is_right_heavy():
            if tallest_child._is_left_heavy():  # Right-Left
                return (self._rotate_left(
                        tallest_child._rotate_right(tallest_child.left)))
            elif tallest_child._is_right_heavy():  # Right-Right
                return self._rotate_left(tallest_child)

    def _rotate_left(self, pivot):
        self.right = pivot.left
        pivot.left = self

        self.height = self._recalculate_height()
        pivot.height = pivot._recalculate_height()
        self.balance_factor = self._calculate_balance_factor()
        pivot.balance_factor = pivot._calculate_balance_factor()

        return pivot

    def _rotate_right(self, pivot):
        self.left = pivot.right
        pivot.right = self

        self.height = self._recalculate_height()
        pivot.height = pivot._recalculate_height()
        self.balance_factor = self._calculate_balance_factor()
        pivot.balance_factor = pivot._calculate_balance_factor()

        return pivot

    def _recalculate_height(self):
        return max(self.left.height if self._has_left_child() else -1,
                   self.right.height if self._has_right_child() else -1) + 1

    def _has_two_children(self):
        return self._has_left_child() and self._has_right_child()

    def _has_left_child(self):
        return self.left is not None

    def _has_right_child(self):
        return self.right is not None

    def _is_balanced(self):
        return self.balance_factor == 0

    def _is_right_heavy(self):
        return self.balance_factor > 0

    def _is_left_heavy(self):
        return self.balance_factor < 0
