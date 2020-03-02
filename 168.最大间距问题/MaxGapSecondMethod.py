# 常规方法一：
#     使用排序算法（如快速排序，基数排序）先处理数组中的数据
#     然后，从已经排序好的数组里面选择间隙最大的数据

import random

class Solution:
    def MaxGap(self, nums):
        if len(nums) < 2:
            value = 0
        
        else:
            nums = Solution().QuickSort(nums)

            value = Solution().GetMaxGapValue(nums)
        
        return value

    # Quickly sorted method calls
    def QuickSortMathod(self, left, right, QuMatrix):
        begin = left
        end = right

        if left > right:
            return

        while left != right:
            if QuMatrix[right] <= QuMatrix[begin]:
                if QuMatrix[left] > QuMatrix[begin]:
                    quickTemp = QuMatrix[left]
                    QuMatrix[left] = QuMatrix[right]
                    QuMatrix[right] = quickTemp

                    right = right - 1
                else:
                    left = left + 1
            else:
                right = right - 1

        
        quickTemp = QuMatrix[begin]
        QuMatrix[begin] = QuMatrix[right]
        QuMatrix[right] = quickTemp

        Solution().QuickSortMathod(begin, (left - 1), QuMatrix)
        Solution().QuickSortMathod((right + 1), end, QuMatrix)

    # Quickly sorted method
    def QuickSort(self, QuMatrix):
        
        Solution().QuickSortMathod(0, (len(QuMatrix) - 1), QuMatrix)
            
        return QuMatrix

    def RadixSort(self, RaMatrix):
        maxValue = Solution().GetMaxValue(RaMatrix)

        list = [[],[], [],[], [],[], [],[], [],[]]

        divisor = 1
        while divisor <= maxValue:
            for RaMaCnt in range (len(RaMatrix)):
                value = (int(RaMatrix[RaMaCnt]/divisor))%10
                bucketCnt = 0
                while bucketCnt < 10:
                    if value == bucketCnt:
                        list[bucketCnt].append(RaMatrix[RaMaCnt])
                        break
                    else:
                        bucketCnt = bucketCnt + 1
            
            RaMatrix = []
            for bucketCnt in range (len(list)):
                for listCnt  in range (len(list[bucketCnt])):
                    RaMatrix.append(list[bucketCnt][listCnt])
                
            divisor = divisor*10
            list = [[],[], [],[], [],[], [],[], [],[]]

        return RaMatrix

    def CountSort(self, CoMatrix):

        maxValue = Solution().GetMaxValue(CoMatrix)

        nums = [0]*(maxValue+1)

        for cnt in range (len(CoMatrix)):
            nums[CoMatrix[cnt]] = nums[CoMatrix[cnt]] + 1

        CoMatrix = []

        for cnt in range(len(nums)):
            if nums[cnt] != 0:
                for count in range(nums[cnt]):
                    CoMatrix.append(cnt)
                    count = count + 1

        return CoMatrix
        
    def GetMaxValue(self, Matrix):
        if len(Matrix) == 0:
            return

        maxValue = Matrix[0]
        for cnt in range (len(Matrix)):
            if maxValue < Matrix[cnt]:
                maxValue = Matrix[cnt]

        return maxValue

    def GetMaxGapValue(self, nums):
        value = 0
        cnt = 0
        while cnt+1 < len(nums):
            if value < (nums[cnt+1] - nums[cnt]):
                value = nums[cnt+1] - nums[cnt]
            cnt = cnt + 1
        
        return value


def RandomInitnums(start, end, length):
    randomnums = []
    for i in range(length):
        randomnums.append(random.randint(start, end))
    
    return randomnums

if __name__ == "__main__":
    Matrix = [1,100]
    min = 1
    max = 40
    number = 4

    # Matrix = RandomInitnums(min, max, number)
    print(Matrix)


    value = Solution().MaxGap(Matrix)
    print(value)