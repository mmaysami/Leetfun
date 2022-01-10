"""
# -------------------------------------------------------------------------------
# Name:         Tree
# Purpose:      Binary Search Tree Utilities
#
#
# Author:       Moe Maysami
#
# Created:      Jan 2020
# Licence:      See Git
# -------------------------------------------------------------------------------
"""


# -------------------------------------------------------------------------------
class TreeNode:
    """
    Binary Search Tree Class

    Assumptions: Left Child < Value < Right Child
    """

    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.value)


# -------------------------------------------------------------------------------
def inorder(root):
    """
    Inorder traversal of BST from root node
    """
    if root is not None:
        inorder(root.left)
        print(root.value, end=',')
        inorder(root.right)


# # -------------------------------------------------------------------------------
def min_value_node(root):
    """
    Return the node with min value found in that tree.

    :param root: Root Node (Instance of TreeNode or None)
    """
    current = root

    # loop down to the leftmost leaf
    while (current.left is not None):
        current = current.left
    return current


# -------------------------------------------------------------------------------
def insert_value(root, value):
    """
    Insert a new node with given value in BST root

    :param root:    Root Node (Instance of TreeNode or None)
    :param value:   Value to Insert in Tree

    """
    # If the tree is empty, return a new node
    if root is None:
        return TreeNode(value)
    # Otherwise, recur down the tree
    if value < root.value:
        root.left = insert_value(root.left, value)
    else:
        root.right = insert_value(root.right, value)

    return root


# -------------------------------------------------------------------------------
def delete_node(root, value):
    """
    Delete the value and returns the new root

    :param root:    Root Node (Instance of TreeNode or None)
    :param value:   Value to Delete from Tree
    """
    if root is None:
        return root

    # deleted value is not same as the root; then search in subtrees
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)

    # If value is same as root, then this is the node
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
        temp = min_value_node(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    return root


# ----------------------------------------------------------------------------
def deserialize(string):
    """
    The input string  [1,null,2,3] represents the serialized format of a binary tree
    using level order traversal, where null signifies a path terminator where no node exists below.

    :param string: String of a list of tree nodes/nulls '[1,2,3,null,null,4,null,null,5]'

    Example:
        []                      Empty Tree
        [1,2,3]                     1
                                   / \
                                  2  3
        [1, null, 2,3]              1
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
            t.write(node.value, align='center', font=('Arial', 12, 'normal'))
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
    from copy import copy, deepcopy

    # drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    # drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))

    n = None
    t1 = TreeNode(5)

    t1.left = TreeNode(3)
    t1.left.left = TreeNode(1)
    t1.left.right = TreeNode(4)

    t1.right = TreeNode(9)
    t1.right.left = TreeNode(7)
    t1.right.right = None

    t2 = deepcopy(t1)
    t2 = insert_value(t2, 8)

    t3 = deepcopy(t1)
    t3 = delete_node(t3, 8)

    cases = [t1, t2, t3]

    for d in cases:
        print('\nData: ', type(d))
        t_inorder = inorder(d)
