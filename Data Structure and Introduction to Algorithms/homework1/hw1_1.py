'''
写一段python程序，计算1+2+3+…+1,000,000，输出计算所需时间。
'''
import time
start = time.time()
n = 1000000
res = 0
for i in range(n):
    res += i+1
end = time.time()

print(f'Sum is {res}, and the calculation took {end-start}s')