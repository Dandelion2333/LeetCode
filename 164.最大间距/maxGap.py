# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

# 如果数组元素个数小于 2，则返回 0。

# 示例 1:

# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
# 示例 2:

# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
# 说明:

# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            value = 0
        
        else:
            maxValue = Solution().GetMaxValue(nums)
            if maxValue < 100000:
                nums = Solution().CountSort(nums)
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