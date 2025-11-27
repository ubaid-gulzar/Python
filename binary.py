#Write a Python function to return the maximum depth (height) of a binary tree.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# Example tree:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print("Max depth:", max_depth(root))
