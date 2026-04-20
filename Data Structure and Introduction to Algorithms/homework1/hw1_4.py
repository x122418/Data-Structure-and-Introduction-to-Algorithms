'''
一个古老的印度神庙里有三根柱，其中一个自上而下放置了由小到大的64个金盘。僧
侣们依照以下规则把 64 个金盘移动到另一
个柱子上： 
• 一次只能移动一个金盘； 
• 金盘只能在柱子上存放； 
• 小盘必须始终放置在大盘上方； 
传说中，64个金盘移动完世界毁灭…… 
请设计并用Python实现算法，接收用户输入的金盘数目N，输出将金盘从柱子0移动
到柱子2的全过程。输出格式为：move(a, x, y)，其中a为盘子编号（1～N），x和y
为柱子编号（0～2），表示将盘子a从柱子x移动到柱子y。
'''

def hanoi(num, source, auxiliary, target):
    if num == 1:
        print(f'move(1, {source}, {target})')
    else:
        hanoi(num-1, source, target, auxiliary)
        print(f'move({num}, {source}, {target})')
        hanoi(num-1, auxiliary, source, target)

n = int(input('input N:'))
hanoi(n, 0, 1, 2)