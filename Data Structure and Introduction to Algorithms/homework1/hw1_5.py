'''
请编写一个python函数，将两个有序的单向链表合并为一个有序链表，合并后使原链
表为空。链表的节点结构参考课件中的单向链表节点，且链表带有哨兵节点作为头节点。
有序链表中元素为从小到大排列。
'''
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def combine(node1, node2):
    node_null = Node()
    cur = node_null
    a, b = node1.next, node2.next
    while a and b:
        if a.val <= b.val:
            cur.next = a
            a = a.next
        else:
            cur.next = b
            b = b.next
        cur = cur.next
    cur.next = a or b
    node1.next = None
    node2.next = None

    return node_null.next