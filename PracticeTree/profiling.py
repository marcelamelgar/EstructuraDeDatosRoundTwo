import cProfile
from binary_tree import Node, BinarySearchTree

# Profile Insert
tree = BinarySearchTree()
cProfile.run('tree.insert(tree.root, 56)')
cProfile.run('tree.insert(tree.root, 12)')
cProfile.run('tree.insert(tree.root, 6)')
cProfile.run('tree.insert(tree.root, 76)')
cProfile.run('tree.insert(tree.root, 23)')

#Profile Search
cProfile.run('tree.search(tree.root, 1)')
cProfile.run('tree.find_max(tree.root)')
cProfile.run('tree.find_min(tree.root)')

#Profile Delete
cProfile.run('tree.delete(tree.root, 32)')