class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
    
    def traverse_in_order(self, root):
        if root:
            self.traverse_in_order(root.left)
            print(root.data)
            self.traverse_in_order(root.right)
            

root = Node(10)
# Tree Structure
#        10
#      /    \
#     None   None

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(20)
root.left.right = Node(45)
root.right.right = Node(54)
root.right.left = Node(2)


# For the tree,
#          10
#        /    \
#       34      89
#     /    \  /    \
#  20     45  2    54

# root.traverse_in_order(root)