


# 解题思路：
#   输入元素小于等于两个时做特殊处理
#   输入元素大于两个时，后面的数据是依赖前面的值计算出来的。然后通过这种滚动的方法一直滚动到最后一个数值。

class Solution:
    def rob(self, nums):
        len_num = len(nums)
        result = 0
        if len_num == 1:
            result = nums[0]
        elif len_num == 2:
            result = max(nums[0], nums[1])
        else:
            num = 3
            # 表示0-倒数第二个的最大值
            value_b = max(nums[0], nums[1])
            # 表示0-倒数第三个的最大值+当前值
            value_g = nums[0] + nums[num-1]

            while (num < len_num):                    
                num = num + 1
                tmp = value_b

                # 表示0-倒数第二个的最大值
                value_b = max(value_g, value_b)

                # 表示0-倒数第三个的最大值
                value_g = tmp + nums[num-1]
            
            result = max(value_g, value_b)
        
        return result

if __name__ == "__main__":
    
    list = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
    # list = [0,0]
    print("value:", Solution().rob(list))
