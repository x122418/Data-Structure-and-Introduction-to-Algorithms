'''
假设一个单链表类使用的节点与课件中的节点相同，但并未记录链表中节点的数目。请
为该类添加一个方法，该方法用于高效找到链表的中间节点。如链表长度为偶数，则返
回两个中间节点中靠后的那一个。
'''
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    def find_mid(self):
        fast = slow = self
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow