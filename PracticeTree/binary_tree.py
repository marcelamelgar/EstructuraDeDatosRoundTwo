class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


    def get_children(self):
        children = []
        if self.left_child is not None:
            children.append(self.left_child.data)
        if self.right_child is not None:
            children.append(self.right_child.data)
        return children


    def visualization(root):
        current_level = [root]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left_child:
                    next_level.append(n.left_child)
                if n.right_child:
                    next_level.append(n.right_child)
            current_level = next_level
        

    def __repr__(self):
        return str(self.data)




class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, root, value):
        if root is None:
            self.root = Node(value)
            return

        if root.data > value:
            if root.left_child is None:
                root.left_child = Node(value)
                return
            else:
                self.insert(root.left_child, value)
        
        if root.data < value:
            if root.right_child is None:
                root.right_child = Node(value)
                return
            else:
                self.insert(root.right_child, value)


    def inorder_traverse(self, root):
        if root is not None:
            self.inorder_traverse(root.left_child)
            print(root.data)
            self.inorder_traverse(root.right_child)
    
  
    def search(self, root, key):
        if root is None:
            return "Key not found in tree :("

        if root.data == key:
            return root
        
        if root.data > key:
            return self.search(root.left_child, key)
        
        if root.data < key: 
            return self.search(root.right_child, key)


    def find_min(self, root):
        current_node = root

        while current_node.left_child is not None:
            current_node = current_node.left_child

        return current_node


    def find_max(self, root):
        current_node = root

        while current_node.right_child is not None:
            current_node = current_node.right_child

        return current_node


    def delete(self, root, key):
        if root == None:
            return root
        if key == root.data:
            if root.left_child == None:
                root = root.right_child
            elif root.right_child == None:
                root = root.left_child
            else:
                root = BinarySearchTree.find_min(root)
                root.right_child = BinarySearchTree.delete(root.right_child, root.key)
        elif key < root.data:
            root.left_child = self.delete(root.left_child, key)
        else:
            root.right_child = self.delete(root.right_child, key)
        return root


tree = BinarySearchTree()
tree.insert(tree.root, 11)
tree.insert(tree.root, 1)
tree.insert(tree.root, 56)
tree.insert(tree.root, 32)
tree.insert(tree.root, 0)
tree.insert(tree.root, 84)
tree.insert(tree.root, 36)
tree.insert(tree.root, -10)
tree.insert(tree.root, 0.2)

print("- Tree -")
Node.visualization(tree.root)
print("- Search -")
print(tree.search(tree.root, 1))
print("- Max -")
print(tree.find_max(tree.root))
print("- Min -")
print(tree.find_min(tree.root))
tree.delete(tree.root, 32)
print("- New Tree - 32 Deleted -")
Node.visualization(tree.root)
