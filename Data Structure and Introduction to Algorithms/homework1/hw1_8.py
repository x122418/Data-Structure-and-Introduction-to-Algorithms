'''
八皇后问题： 
请设计并用 Python 实现一个算法，找出所有在8×8的国际象棋棋盘上放置皇后的方
式，使得这些皇后互相之间不能处于可互吃的状态。（20分） 
（注：皇后是国际象棋所有棋子中威力最大的，可以吃掉与其同一行、列、或对角线上
的棋子）
'''

# 以前刷leetcode做过N皇后
def solveNQueens(self, n: int) -> List[List[str]]:
        col = [0] * n  # 存储每一行 对应Q所在的列
        col_path = [0] * n    # 记录 哪些列已经被占据

        left = [0] * (2*n - 1)
        rig = [0] * (2*n - 1)
        ans = []

        def dfs(i):
            # 考虑到idx i 的行
            if i == n:
                ans.append( [ '.' * num +  'Q' + '.' * (n - num -1)   for num  in col ]  )
                return 
            for j in range(n):
                if col_path[j] == 0 and rig[i + j] == 0 and left[i - j + n - 1] == 0:
                    col_path[j] = 1
                    rig[i + j] = 1
                    left[i - j + n - 1] = 1
                    col[i] = j
                    dfs(i + 1)
                    col_path[j] = 0
                    rig[i + j] = 0
                    left[i - j + n - 1] = 0

        dfs(0)
        return ans