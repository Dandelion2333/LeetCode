


class Solution:
    def productExceptSelf(self, nums):
        value = 1
        zeroCnt = 0

        for cnt in range (len(nums)):
            if nums[cnt] != 0:
                value = nums[cnt] * value
            else:
                zeroCnt = zeroCnt + 1

        
        for cnt in range (len(nums)):
            if zeroCnt <= 1:
                if nums[cnt] != 0:
                    nums[cnt] = int(value / nums[cnt])
                else:
                    nums[cnt] = value
            else:
                nums[cnt] = 0

        return nums


if __name__ == "__main__":
    list = [1,0] 
    print(list)

    list = Solution().productExceptSelf(list)   

    print(list)





