class QuadraticProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()       # sentinal marks locations of previous deletions
    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is QuadraticProbeHashMap._AVAIL

    # 二次探测
    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        i = 0
        while True:                               
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j                      # mark this as first avail
                if self._table[j] is None:
                    return (False, firstAvail)          # search has failed
            elif k == self._table[j]._key:
                return (True, j)                      # found a match
            i += 1
            j = (j + 2*i - 1 ) % len(self._table)          # keep looking (cyclically)
      
    # 再哈希法
class DoubleHashMap(HashMapBase):
    _AVAIL = object()       # 标记已删除的位置

    def __init__(self, cap=11, p=109345121, q=7):
        """
        cap: 初始桶数组大小（建议为质数）
        p:   MAD 压缩用的大质数
        q:   第二个哈希函数的模数（质数，且小于 cap）
        """
        super().__init__(cap, p)
        self._q = q

    def _h2(self, k):
        """h2(k) = q - (k mod q)"""
        return self._q - (hash(k) % self._q)

    def _find_slot(self, j, k):
        """
        使用双重哈希探测。
        返回 (success, index)：
          - 如果找到键 k，success = True, index 为其位置。
          - 如果未找到，success = False, index 为第一个可用的空位（None 或 _AVAIL）。
        """
        firstAvail = None
        i = 0
        step = self._h2(k)
        start = j                   # 原始哈希地址
        while True:
            curr = (start + i * step) % len(self._table)
            if self._is_available(curr):
                if firstAvail is None:
                    firstAvail = curr
                if self._table[curr] is None:
                    return (False, firstAvail)
            elif k == self._table[curr]._key:
                return (True, curr) 
            i += 1