'''
给出类HeapPriorityQueue中_upheap和_downheap方法的非递归实现。
'''
class HeapPriorityQueue:
    def __init__(self):
        self._data:list[int] = []
    
    def swap(self,i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        while j > 0:
            parent = (j-1) // 2
            if self._data[j] < self._data[parent]:
                self.swap(j, parent)
            else:
                break
            j = parent

    def _downheap(self, j):
        n = len(self._data)
        while True:
            left = 2 * j + 1
            right = 2 * j + 2
            smallest = j

            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == j:
                break
            self.swap(j, smallest)
            j = smallest