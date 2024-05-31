
from collections import deque

class monot_dequeue:

    # 构造函数，用于设置对象的初始状态
    def __init__(self):
        self.deque = deque()

    def push(self, value):
        # 把小于value的值全部弹出
        while self.deque and self.deque[-1] < value:
            # 弹出右侧的数据，默认左边大，右边小，是单调递减队列
            self.deque.pop()    
        self.deque.append(value)

    # 判断value是否等于最大值，假如是则弹出
    def pop(self, value):

        # 在头部弹出元素
        if self.deque and self.deque[0] == value:
            self.deque.popleft()

    def get_max(self):
        return self.deque[0] if self.deque else None
        # if self.deque:
        #     # 返回最大值
        #     return self.deque[0]
        # else:
        #     return None

# 创建对象
monot = monot_dequeue()

monot.push(3)
monot.push(4)
monot.push(-1)

value = monot.get_max()
print(value)

    



