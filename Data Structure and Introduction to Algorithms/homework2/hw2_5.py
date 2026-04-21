'''
如果充分利用哨兵节点（_sentinel），我们可以简化链式二叉树 LinkedBinaryTree
的实现过程。这里，哨兵节点为根节点的父节点，且根节点为哨兵节点的左孩子节点。
请写出新的LinkedBinaryTree的_delete 方法。
'''

def _delete(self, p):
    """Delete the node p, and replace it with its child, if any.
    Return the element that had been stored at p.
    Raise ValueError if p is invalid or p has two children.
    """
    if p is self._sentinel or p is None:
        raise ValueError('Invalid node')

    if self.num_cildren(p) == 2:
        raise ValueError('Node has two children')
    
    child = p._left if p._left else p._right # might be None

    if child is not None:
        child._parent = p._parent
    
    if p is p._parent.left:
        p._parent._left = child
    else:
        p._parent._right = child
    
    self._size -= 1
    p._parent = p                    # convention for deprecated node
    return p._element
