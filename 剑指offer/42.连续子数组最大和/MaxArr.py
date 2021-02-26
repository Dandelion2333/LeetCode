"""
题目：
    输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
    要求时间复杂度为O(n)。

    示例1:

    输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


解题思路：
    思路一：使用两层循环，遍历数组，获取最大的值。但是题目要求时间复杂度为O(n)，所以这个思路被pass
    思路二：只遍历一边，遍历时动态调整数据。
        1、sub_max_val负责子数组的累加
        2、all_max_val只能通过子数组更新，不能通过其他方式更改

进度：
    python：进行中
    C++：还未开始

执行结果：
    未记录
"""

class Solution1:
    def maxSubArray(nums):
        all_max_val = 0         # 用于保存所有子数组中最大的累加和
        sub_max_val = 0         # 用于保存某一段子数组数值的累加，当一个子数组结束时清空此变量

        # 特殊情况处理
        if len(nums) == 1:
            return nums[0]
        else:
            # 处理第一个值
            sub_max_val = sub_max_val + nums[0]
            all_max_val = sub_max_val

        for cnt in range(1, len(nums)):
            if nums[cnt] > 0:
                if sub_max_val < 0:
                    if sub_max_val < nums[cnt]:
                        # 更新子数组
                        sub_max_val = nums[cnt]
                else:
                    sub_max_val = sub_max_val + nums[cnt]
            else:
                # 子数组是正数的情况
                if sub_max_val > 0:
                    # nums[cnt]的绝对值比前者大，证明可以重新累加，因为此时累加已经成为了负值，当前子数组结束
                    if sub_max_val + nums[cnt] < 0:
                        # 清空上一个子数组
                        sub_max_val = 0
                    # 当后者的绝对值比前者小，证明可以继续累加。因为到现在为止，子数组累加有正值
                    else:
                        sub_max_val = sub_max_val + nums[cnt]
                # 子数组是非正的情况
                else:
                    if sub_max_val < nums[cnt]:
                        # 更新子数组
                        sub_max_val = nums[cnt]

            # 更新实际最大值
            if sub_max_val > all_max_val:
                all_max_val = sub_max_val
                

        return all_max_val

if __name__ == "__main__":
    nums = [-2,-1,-3]

    print(Solution1.maxSubArray(nums))