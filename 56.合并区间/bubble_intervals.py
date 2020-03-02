# 合并间隔
# 给定间隔的集合，合并所有重叠的间隔。
# 给定间隔的集合，合并所有重叠的间隔。

# 范例1：
#     输入： [[1,3]，[2,6]，[8,10]，[15,18]]
#     输出： [[1,6]，[8,10]，[15,18]]
#     说明：由于间隔[1,3]和[2,6]重叠，因此将它们合并为[1,6]。

# 范例2：
#     输入： [[1,4]，[4,5]]
#     输出： [[1,5]]
#     说明：间隔[1,4]和[4,5]被认为是重叠的。

# 我的实现方式为冒泡排序的思想

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        leftCnt = 0
        rightCnt = 0
        while leftCnt < len(intervals):
            rightCnt = leftCnt + 1
            while (rightCnt) < len(intervals):
                if (intervals[leftCnt][0] >= intervals[rightCnt][0] and intervals[leftCnt][0] <= intervals[rightCnt][1]) \
                or (intervals[leftCnt][1] >= intervals[rightCnt][0] and intervals[leftCnt][1] <= intervals[rightCnt][1]) \
                or (intervals[leftCnt][0] <= intervals[rightCnt][0] and intervals[leftCnt][1] >= intervals[rightCnt][1]) :
                    if intervals[leftCnt][0] > intervals[rightCnt][0]:
                        intervals[leftCnt][0] = intervals[rightCnt][0]
                    if intervals[leftCnt][1] < intervals[rightCnt][1]:
                        intervals[leftCnt][1] = intervals[rightCnt][1]

                    del intervals[rightCnt]   
                    rightCnt = leftCnt + 1
                else:
                    rightCnt = rightCnt + 1  
            
            leftCnt = leftCnt + 1

        return intervals