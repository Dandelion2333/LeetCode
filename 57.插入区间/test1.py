class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        leftCnt = 0
        rightCnt = 0

        # Insert left value into array
        while newInterval[0] > intervals[leftCnt][1]:
            leftCnt = leftCnt + 1
        
        if newInterval[0] < intervals[leftCnt][0]:
            leftValue = newInterval[0]
        else:
            leftValue = intervals[leftCnt][0]
        mergeStart = leftCnt

        # Insert right value into array
        rightCnt = leftCnt
        while (rightCnt < len(intervals)) and (newInterval[1] > intervals[rightCnt][1]):
            rightCnt = rightCnt + 1
                
        if rightCnt < len(intervals):
            if newInterval[1] < intervals[rightCnt][0]:
                rightValue = newInterval[1]
                mergeEnd = rightCnt
            else:
                rightValue = intervals[rightCnt][1]
                mergeEnd = rightCnt+1
        else:
            rightValue = newInterval[1]
            mergeEnd = rightCnt

        intervals.insert(mergeEnd, [leftValue,rightValue])
        
        # Merge coincident intervals
        deleteCnt = 0
        while deleteCnt < (mergeEnd-mergeStart):
            del intervals[mergeStart]
            deleteCnt = deleteCnt + 1