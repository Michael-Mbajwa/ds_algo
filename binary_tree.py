# A class for an individual node in a binary tree
class Node:
    def __init__(self, key):
        self.root = key
        self.left = None
        self.right = None


# Insertion in a binary tree in level order
# Given a binary tree and a key, insert the key into the binary tree at the first position available in level order.
def inorder_transversal(node):
    if not node:
        return
    print(node.root, end=" ")
    inorder_transversal(node.left)
    inorder_transversal(node.right)


# Function to insert element in binary tree
def binary_tree_insert(node, key):
    if not node:
        root = Node(key)
        return

    # We will now transverse until we find an empty space
    q = [node]
    while len(q):
        node = q.pop(0)
        if not node.left:
            node.left = Node(key)
            break
        else:
            q.append(node.left)
        if not node.right:
            node.right = Node(key)
            break
        else:
            q.append(node.right)


# Deletion in Binary Tree
# Given a binary tree, delete a node from it by making sure that tree shrinks from the bottom (i.e. the deleted node
# is replaced by the bottom-most and rightmost node).
def delete_deepest(root, node):
    """
    Function to delete the deepest node.
    :param root: The binary tree.
    :param node: Deepest node to be deleted.
    :return: ""
    """
    q = [root]
    while len(q):
        temp = q.pop(0)
        if temp is node:
            temp = None
            return
        if temp.right:
            if temp.right is node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is node:
                temp.left = None
                return
            else:
                q.append(temp.left)


def deletion(root, key):
    """
    function to delete element from a binary tree
    :param root:
    :param key: Element to be deleted
    :return:
    """
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.root == key:
            return None
        else:
            return root
    key_node = None
    q = [root]
    temp = None
    while len(q):
        temp = q.pop(0)
        if temp.root == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.root
        delete_deepest(root, temp)
        key_node.root = x
    return root


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Before deletion: ", end="")
    inorder_transversal(root)

    root = deletion(root, 12)
    print()
    print("After deletion: ", end="")
    inorder_transversal(root)