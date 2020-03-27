'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

'''

class Solution:
    def findMedianValue(self, nums1, nums2):
        midValue = 0
        num = nums1 + nums2

        num = Solution().CountSort(num)

        print("排序后的数据",num)

        rightCnt = int(len(num)/2 - 1)
        midCnt = int(len(num)/2)
        leftCnt = int(len(num)/2)
        #print(rightCnt, leftCnt, midCnt)

        if len(num) % 2 == 0:
            midValue = (num[rightCnt] + num[leftCnt]) / 2
        else:
            midValue = num[midCnt]

        return midValue

    def CountSort(self, CoMatrix):
        maxValue = Solution().GetMaxValue(CoMatrix)
        minValue = Solution().GetMinValue(CoMatrix)

        # 准备一个可容纳数组中所有数的list，空间为 maxValue - minValue
        list = [0]*(maxValue - minValue + 1)

        # 把matrix中的数据个数对应到list中
        for cnt in range (len(CoMatrix)):
            # 增加偏移量为最小的数
            list[CoMatrix[cnt] - minValue] = list[CoMatrix[cnt] - minValue] + 1

        CoMatrix = []

        # 把list中的数据，非0的部分放入matrix中
        for cnt in range(len(list)):
            if list[cnt] != 0:
                # 把list中保存元素的个数一一赋值到matrix中
                for count in range(list[cnt]):
                    CoMatrix.append(cnt + minValue)
                    # count = count + 1
        return CoMatrix

    def GetMaxValue(self, Matrix):
        if len(Matrix) == 0:
            return

        maxValue = Matrix[0]
        for cnt in range (len(Matrix)):
            if maxValue <= Matrix[cnt]:
                maxValue = Matrix[cnt]

        return maxValue

    def GetMinValue(self, Matrix):
        if len(Matrix) == 0:
            return

        minValue = Matrix[0]

        for cnt in range (len(Matrix)):
            if minValue >= Matrix[cnt]:
                minValue = Matrix[cnt]

        return minValue                                     


if __name__ == "__main__":
    nums1 = [-3,0]

    nums2 = [-2,-1]

    val = Solution().findMedianValue(nums1, nums2)
    
    print(val)