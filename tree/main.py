# Ben's BST

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
    def __str__(self):
        if not self.left and not self.right: # leaf node
            return str(self.data)
        else:
            left_str = str(self.left) if self.left else "_"
            right_str = str(self.right) if self.right else "_"
            return "(" + left_str + " " + str(self.data) + " " + right_str + ")"
 

class BST:
    def __init__(self, x):
        self.root = Node(x)

    def __str__(self):
        return self.root.__str__()

    def insert(self, val):
        # if(self.exists(val)):
        #     return 
        self.insert_node(self.root, val)

    def insert_node(self, node, val):
        if(node.data == val):
            return
        if(val > node.data):
            if(node.right == None):
                node.right = Node(val)
                return
            return self.insert_node(node.right, val)
        else:
            if(node.left == None):
                node.left = Node(val)
                return
            return self.insert_node(node.left, val)

    def nth_smallest(self,n):
        value, count = self.nth_smallest_search(self.root, n, 0, None)
        return value
    
    def nth_smallest_search(self, node, limit, count, value):
        if(node.left != None):
            value, count = self.nth_smallest_search(node.left, limit, count, value)
        count += 1
        if(count == limit):
            return node.data, count 
        if(node.right != None):
            return self.nth_smallest_search(node.right, limit, count, value)

        return value, count

    

bst = BST(8)
bst.insert(3)
assert bst.root.left.data == 3, "should have been inserted"
bst.insert(1)
assert bst.root.left.left.data == 1, "should have been inserted"
bst.insert(6)
bst.insert(10)
bst.insert(14)
bst.insert(13)
bst.insert(4)
bst.insert(7)


for n in range(0, 10):
    print(bst.nth_smallest(n))
