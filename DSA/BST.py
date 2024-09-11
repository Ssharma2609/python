class Node:
    def __init__(self, key):
        """Initialize a node with a given key and no children."""
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        """Initialize an empty Binary Search Tree."""
        self.root = None

    def insert(self, key):
        """Insert a new node with the given key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """Helper method to insert a new node recursively."""
        if key < current_node.value:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.value:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def search(self, key):
        """Search for a node with the given key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        """Helper method to search for a key recursively."""
        if current_node is None or current_node.value == key:
            return current_node is not None
        if key < current_node.value:
            return self._search_recursive(current_node.left, key)
        return self._search_recursive(current_node.right, key)

    def inorder_traversal(self):
        """Return a list of values obtained from an in-order traversal."""
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        """Helper method for in-order traversal."""
        result = []
        if current_node is not None:
            result = self._inorder_recursive(current_node.left)
            result.append(current_node.value)
            result += self._inorder_recursive(current_node.right)
        return result

# Example usage:
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    
    print("In-order Traversal:", bst.inorder_traversal())  # Should print sorted values
    print("Search for 5:", bst.search(5))  # Should return True
    print("Search for 3:", bst.search(3))  # Should return False
