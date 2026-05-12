'''
给出类HeapPriorityQueue中_upheap和_downheap方法的非递归实现。
'''

class HeapPriorityQueue:
    def __init__(self):
        self._data: list[int] = []

    def _upheap(self, j):
        while j > 0:
            parent = (j - 1) // 2
            if self._data[j] < self._data[parent]:
                self._data[j], self._data[parent] = self._data[parent], self._data[j]
                j = parent
            else:
                break

    def _downheap(self, j):
        n = len(self._data)
