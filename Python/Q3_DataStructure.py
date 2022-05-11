# - What data structure does a binary tree degenerate to if it is not balanced properly in python ?
# - A linked list. LL is a collection of nodes. Each node contains the data element and a pointer to the
#next node. Nodes can be added and deleted dynamically.
# - In co,puter science a binary tree is a tree data structure in which each node has at
#most two children, which are referred to as the left child and the right child

from binarytree import Node

root = Node(3)
root.left = Node(6)
root.right = Node(8)

print('Binary tree: ', root)
print('List of nodes: ', list(root))
print('Properties: ', root.properties)