
# 解题思路：
#   采用递归的方法：要求任意k位置的最大金额，需要知道f(k-1)与f(k-2)+nums[k-1]的值（取最大值即可）
#   通过递归的方式分别求f(k-1)与f(k-2)，知道f(0)与f(1)为止

class Solution:
    def rob(self, nums):
        f = []
        len_num = len(nums)
        Solution().init_array(f, len_num)

        # 给定f1-f4的数值
        if len_num >= 4:
            Solution().init_f4(nums, f)

        return Solution().rob_new(nums, f)

    def rob_new(self, nums, f):    
        len_num = len(nums)    
        if len_num <= 4:
            value = Solution().get_less_f4(nums, f)
        else:
            value = Solution().get_greater_f4(nums, f)

        # print("list:",f)
        # print("value:",value)
        return value

    # 当元素个数大于四个时
    def get_greater_f4(self, nums, f):
        # cnt表示下标
        cnt = len(nums) - 1
        # len_num表示数组长度
        len_num = len(nums)
        
        # 0至cnt-2的最大值 + f(cnt)本身
        if f[cnt-2] == -1:
            list1 = nums[0:len_num-2]
            # 获取0-倒数第三个的数值
            f[cnt-2] = Solution().rob_new(list1, f)
        f[cnt] = f[cnt-2] + nums[cnt]
        value1 = f[cnt]

        # 0至cnt-1的最大值
        if f[cnt-1] == -1:
            list2 = nums[0:len_num-1]
            f[cnt-1] = Solution().rob_new(list2, f)
        value2 = f[cnt-1]

        if value1 > value2:
            return value1
        else:
            return value2

    # 当元素个数小于等于四个时
    def get_less_f4(self, nums, f):
        len_num = len(nums)
        if(len_num == 1):
            f[0] = nums[0]
            return f[0]
        elif(len_num == 2):
            return Solution().get_nums2(nums, f)
        elif(len_num == 3):
            return Solution().get_nums3(nums, f)
        else:
            return Solution().get_nums4(nums, f)

    def get_nums2(self, nums, f):
        if nums[0] > nums[1]:
            f[1] = nums[0]
        else:
            f[1] = nums[1]
        return f[1]
    
    def get_nums3(self, nums, f):
        value = nums[0] + nums[2]
        if value > nums[1]:
            f[2] = value
        else:
            f[2] = nums[1]
        return f[2]

    def get_nums4(self, nums, f):
        value1 = nums[0] + nums[2]
        value2 = nums[1] + nums[3]
        value3 = nums[0] + nums[3]

        if value1 > value2:
            f[3] = value1
        else:
            f[3] = value2
        
        if f[3] < value3:
            f[3] = value3
        return f[3]

    def init_array(self, f, nums):
        for cnt in range(nums):
            f.append(-1)

    def init_f4(self, nums, f):
        f[0] = nums[0]
        Solution().get_nums2(nums, f)
        Solution().get_nums3(nums, f)
        Solution().get_nums4(nums, f)

        # print(f)

if __name__ == "__main__":
    
    list = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
    # list = [3,2,12,8,4,9,10]
    # list = [183,219,57,193,94]
    
    print("value:", Solution().rob(list))
