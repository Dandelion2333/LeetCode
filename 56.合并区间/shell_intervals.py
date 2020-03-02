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

# 我的实现方式为希尔排序的思想
def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    delete = []
    gapNum = 2

    gap = int((len(intervals) / gapNum))
    
    while gap > 0:
        begin = 0
        # Set each data loop
        while begin < gap:
            leftCnt = begin
            rightCnt = begin + gap

            # Sorting of each group of data after separation by gaps
            while rightCnt < len(intervals):
                if (intervals[leftCnt][0] >= intervals[rightCnt][0] and intervals[leftCnt][0] <= intervals[rightCnt][1]) \
                or (intervals[leftCnt][1] >= intervals[rightCnt][0] and intervals[leftCnt][1] <= intervals[rightCnt][1]) \
                or (intervals[leftCnt][0] <= intervals[rightCnt][0] and intervals[leftCnt][1] >= intervals[rightCnt][1]) :
                    if intervals[leftCnt][0] > intervals[rightCnt][0]:
                        intervals[leftCnt][0] = intervals[rightCnt][0]
                    if intervals[leftCnt][1] < intervals[rightCnt][1]:
                        intervals[leftCnt][1] = intervals[rightCnt][1]

                    intervals[rightCnt][0] = 'd'

                rightCnt =  rightCnt + gap

            begin = begin + 1

        if DeleteData(intervals) == 1:
            gapNum = gapNum
        else:
            gapNum = gapNum * 2
        
        gap = int((len(intervals) / gapNum))

    intervals = merge1(intervals)

    return intervals

def merge1(intervals):
    inCnt = 0
    rightCnt = 0
    while inCnt < len(intervals):
        rightCnt = inCnt + 1
        while (rightCnt) < len(intervals):
            if (intervals[inCnt][0] >= intervals[rightCnt][0] and intervals[inCnt][0] <= intervals[rightCnt][1]) \
            or (intervals[inCnt][1] >= intervals[rightCnt][0] and intervals[inCnt][1] <= intervals[rightCnt][1]) \
            or (intervals[inCnt][0] <= intervals[rightCnt][0] and intervals[inCnt][1] >= intervals[rightCnt][1]) :
                if intervals[inCnt][0] > intervals[rightCnt][0]:
                    intervals[inCnt][0] = intervals[rightCnt][0]
                if intervals[inCnt][1] < intervals[rightCnt][1]:
                    intervals[inCnt][1] = intervals[rightCnt][1]

                del intervals[rightCnt]   
                rightCnt = inCnt + 1
            else:
                rightCnt = rightCnt + 1  
        
        inCnt = inCnt + 1

    return intervals

def DeleteData(intervals):
    deleteNum = 0  
    deleteFlag = 0
    while deleteNum < len(intervals):
        if intervals[deleteNum][0] == 'd':
            del intervals[deleteNum]
            deleteFlag = 1
        else:
            deleteNum = deleteNum + 1

    return deleteFlag

if __name__ == "__main__":

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = merge(intervals)

    print(result)