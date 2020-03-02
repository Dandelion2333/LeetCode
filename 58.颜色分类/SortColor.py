class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        Solution.QuickSort(nums, 0, (len(nums)-1))

    def QuickSort(List, start, end):
        if start > end:
            return

        left = start
        right = end

        while left != right:
            if List[right] > List[start]:
                right = right - 1
            else:
                if List[left] <= List[start]:
                    left = left + 1
                else:
                    Solution.Swap(List, left, right)
                    right = right - 1            
        
        Solution.Swap(List, start, right)

        Solution.QuickSort(List, start, left-1)
        Solution.QuickSort(List, right+1, end)

    def Swap(list, left, right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp

class SolutionSelect:
    def sortColors(self, nums):
        zero = []
        one = []
        two = []

        for cnt in range(len(nums)):
            if nums[cnt] == 0:
                zero.append(nums[cnt])
            elif nums[cnt] == 1:
                one.append(nums[cnt])
            else:
                two.append(nums[cnt])
        
        nums = zero + one + two
        print(nums)

class SolutionPointer:
    def sortColors(self, nums):
        p0 = 0
        p2 = len(nums) - 1
        numsCnt = 0

        while numsCnt <= p2:
            if nums[numsCnt] == 0:
                while p0 < len(nums) and nums[p0] == 0:
                    p0 = p0 + 1
                if p0 <= numsCnt:
                    SolutionPointer.Swap(nums, p0, numsCnt)
                    p0 = p0 + 1

                print("p1")
                print(p0, numsCnt, nums) 

            elif nums[numsCnt] == 2:
                while p2 > 0 and nums[p2] == 2:
                    p2 = p2 - 1
                if numsCnt <= p2:
                    SolutionPointer.Swap(nums, numsCnt, p2)
                    p2 = p2 - 1  

                if numsCnt > 0 and nums[numsCnt] == 0:
                    numsCnt =  numsCnt - 1     
                
                print("p2")
                print(p2, numsCnt, nums)   
            numsCnt = numsCnt + 1    
              

    def Swap(list, left, right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp

if __name__ == "__main__":
    List = [2,1,2]

    #Solution().sortColors(List)
    #SolutionSelect().sortColors(List)
    SolutionPointer().sortColors(List)