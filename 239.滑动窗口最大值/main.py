'''
## 问题分析
该问题可以分解成两个步骤。
1. 滑块向右移动，移动的过程中，每次都需要获取滑块中的最大值
2. 获取滑块最大值成为关键。
采用暴力破解的方法，时间复杂度为O(nk)。
## 我的方法
1. 计算第一次滑块的最大值MAX。
2. 滑块每次移动时，只会改变最左侧与最右侧两个值
3. 当最左侧为上次的最大值时，需要重新计算滑块的最大值
4. 当最右侧为最大值时，则更新MAX。
该方法的弊端。即第三点，有些情况下需要重新计算，会增加时间的消耗。

## 网友的方法
他的核心有两点
1. 不要维护滑块的值
2. 把最大值始终放在队列的第一个。就不会有我第三点的问题了。
为了便于维护，采用了队列解决。值得注意的是，采取的是双向队列，队列的尾部也可以弹出数据。

## 我的总结
解题的方式可以分成几个步骤，每个步骤都是子模块，每个子模块都有一套对应的解决方法。
例如该问题分成两个子模块
1. 从左滑到右，时间复杂度是On。用普通的循环解决即可。
2. 需要从K个数中选出最大值。所以这部分的时间复杂度越低越好。暴力法的时间复杂度是Ok，单调栈的为Ologk。
随着解题越来越多，就会积累更多的子模块处理方法。而同样的子模块会应用到其他题目中。
'''

class Solution:
    def maxSlidingWindow(self, nums, k):

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
                if self.deque and self.deque[0] == value:
                    
                    # 弹出最左侧数据
                    self.deque.popleft()

            def get_max(self):
                if self.deque:
                    # 返回最大值
                    return self.deque[0]
                else:
                    return None
        
        # 创建单调递减队列，左侧为最大值，向右侧单调递减
        monot = monot_dequeue()
        # 创建最大值数组
        max_list = []

        # 把0-k个元素放入队列
        for i in range(k):
            monot.push(nums[i])
        # 获取第一个滑动窗口的最大值
        max_list.append(monot.get_max())

        right = k   # 此处已经取到K值作为下标
        left = 0    # 此处把第一个元素作为下标，因为下面的while循环会把它作为滑块的离开值
        
        # 遍历数组
        while right < len(nums):
            # 把新值push到队列中，monot类会维系单点递减队列
            monot.push(nums[right])

            # 把滑块离开值弹出
            monot.pop(nums[left])
            
            # 把当前最大值存入max_list中
            max_list.append(monot.get_max())
            right = right + 1
            left = left + 1

        return max_list


if __name__ == "__main__":
    
    # list = [1,3,-1,-3,5,3,6,7]
    list = [1, -1]
    k = 1

    max_list = Solution().maxSlidingWindow(list, k)  
    print(max_list)