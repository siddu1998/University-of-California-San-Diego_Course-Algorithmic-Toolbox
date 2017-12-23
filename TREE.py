class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(4)
root.right.left=Node(5)

root.left.right=Node(6)
root.left.left=Node(7)
    