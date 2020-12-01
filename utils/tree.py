"""
# -------------------------------------------------------------------------------
# Name:         Tree
# Purpose:      Binary Tree Utilities
#
#
# Author:       Moe Maysami
#
# Created:      Jan 2020
# Licence:      See Git
# -------------------------------------------------------------------------------
"""


# ----------------------------------------------------------------------------
class TreeNode:
    """
    Binary Tree Class
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


# ----------------------------------------------------------------------------
def inorder(root):
    """
    Inorder traversal of BST from root node
    """
    if root is not None:
        inorder(root.left)
        print
        root.key,
        inorder(root.right)


# ----------------------------------------------------------------------------
def insert(root, key):
    """
    Insert a new node with given key in BST root

    :param root: Root Node (Instance of TreeNode or None)
    :param key:  Value to Insert in Tree

    """
    # If the tree is empty, return a new node
    if root is None:
        return TreeNode(key)
    # Otherwise recur down the tree
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# ----------------------------------------------------------------------------
def minValueNode(root):
    """
    Return the node with min key value found in that tree.

    :param root: Root Node (Instance of TreeNode or None)
    """
    current = root

    # loop down to the leftmost leaf
    while (current.left is not None):
        current = current.left
    return current


# ----------------------------------------------------------------------------

def deleteNode(root, key):
    """
    Delete the key and returns the new root

    :param root: Root Node (Instance of TreeNode or None)
    :param key:  Value to Insert in Tree
    """
    if root is None:
        return root

    # deleted key is not same as the root; then search in subtrees
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)

    # If key is same as root, then this is the node
    else:
        # a/b. Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # c. 2 children: Get the inorder successor (smallest in right sub)
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root


# ----------------------------------------------------------------------------
def deserialize(string):
    """

    The input string  [1,null,2,3] represents the serialized format of a binary tree
    using level order traversal, where null signifies a path terminator where no node exists below.

    :param string: String of a list of tree nodes/nulls '[1,2,3,null,null,4,null,null,5]'

    Example:
        []
        Empty Tree

        [1,2,3]
            1
           / \
          2  3

        [1, null, 2,3]
            1
             \
             2
            /
           3
    """

    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


# ----------------------------------------------------------------------------
def drawtree(root):
    """
    Visualize Trees

    :param root: Root Node (Instance of TreeNode or None)
    """

    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
