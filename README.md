# pyvl-tree

__pyvl-tree__ is an a self-balancing binary search tree (BST) implemented using the Adelson-Velsky & Landis (AVL) algorithms.

A self-balancing BST has the valuable property that its height is _at most_ __log<sub>2</sub>(n)__, 
where __n__ is the number of elements in the tree. This means that _search_, _insertion_ and _deletion_ 
has more reliable performance than an ordinary BST as the number of elements in the tree increases.

## Install
Install with,

```
pip install pyvl-tree
```

## API

### `class pyvltree.AVLTree`
A recursive implementation of a self-balancing binary search tree. Self-balancing is achieved using the AVL algorithms.

#### `AVLTree()`
Constructor. Creates a AVLTree object and returns it.

#### `search(key)`
Search for an element given an equivalent key.

Equivalence is determined based on the elements `__eq__` method.

Average time complexity: O(log n)
Worst-case time complexity: O(log n)

Returns the element equivalent to the key if found, `None` otherwise.

#### `size()`
Calculates the number of elements in the tree.

Time complexity: O(n)

Returns the number of elements in the tree.

#### `insert(obj)`
Insert an element into the tree.

Duplicate elements will be silently discarded.

Average time complexity: O(log n)
Worst-case time complexity: O(log n)

#### `delete(obj)`
Deletes an element from the tree.

If the element deleted had two children, it will be replaced by its in-order successor.

Average time complexity: O(log n)
Worst-case time complexity: O(log n)

## Performance
![Plot linear](./perf/plot-linear.png)

![Plot logarithmic](./perf/plot-log.png)