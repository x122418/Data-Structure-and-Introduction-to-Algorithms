'''
请根据课件上给出的双端队列的ADT，给出一个完整的基于数组的双端队列的 python
实现。
'''
class deque:
    def __init__(self):
        self.data = []

    def add_first(self, e):
        self.data.insert(0, e)

    def add_last(self, e):
        self.data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Exception("双端队列为空")
        return self._data.pop(0)
    
    def delete_last(self):
        if self.is_empty():
            raise Exception("双端队列为空")
        return self._data.pop()
    
    def first(self):
        if self.is_empty():
            raise Exception("双端队列为空")
        return self._data[0]
    
    def last(self):
        if self.is_empty():
            raise Exception("双端队列为空")
        return self._data[-1]
    
    def __len__(self):
        return len(self.data)
    
    def init(self, D):
        self.data = D.data
    
    def is_empty(self):
        return len(self) == 0

    def clear(self):
        self._data = []    