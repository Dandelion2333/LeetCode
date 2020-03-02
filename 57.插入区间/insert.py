class Solution(object):
    def insert(self, intervals, newInterval):
        # Entry parameter check
        if (len(intervals) > 0) and (len(newInterval) == 2):
            intervals = Solution.InsertLeft(intervals, newInterval)
        else:
            if len(intervals) == 0:
                intervals.append(newInterval)

        return intervals

    def InsertLeft(intervals, newInterval):
        # Insert left value into array
        leftCnt = 0

        while (leftCnt < len(intervals)) and (newInterval[0] > intervals[leftCnt][1]):
            leftCnt = leftCnt + 1
        
        if leftCnt < len(intervals):
            if newInterval[0] < intervals[leftCnt][0]:
                leftValue = newInterval[0]
            else:
                leftValue = intervals[leftCnt][0]

            intervals, mergeEnd = Solution.InsertRight(intervals, newInterval, leftCnt, leftValue)

            intervals = Solution.Merge(intervals, leftCnt, mergeEnd)
        else:
            intervals.insert(leftCnt, newInterval)
        
        return intervals

    def InsertRight(intervals, newInterval, leftCnt, leftValue):
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

        return intervals, mergeEnd
    
    def Merge(intervals, mergeStart, mergeEnd):
        # Merge coincident intervals
        deleteCnt = 0
        while deleteCnt < (mergeEnd-mergeStart):
            del intervals[mergeStart]
            deleteCnt = deleteCnt + 1
        
        return intervals

if __name__ == "__main__":

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]

    result = Solution().insert(intervals, newInterval)

    print(result)