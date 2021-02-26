"""
题目：
    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    示例 1:
    输入: 121
    输出: true

    示例 2:
    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

    示例 3:
    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。

解题思路：
    定义两个指针，分别指向输入变量的头与尾，然后从以次比对指针指向的数据是否相同

进度：
    python：已经完成
    C++：还未开始

执行结果：
    执行用时：
    64 ms, 在所有 Python3 提交中击败了92.25%的用户
    内存消耗：
    15 MB, 在所有 Python3 提交中击败了5.01%的用户
"""


class Solution:
    def isPalindrome(input_val):
        s_input_val = str(x)
        right_index = len(s_input_val) - 1
        left_index = 0
        flag = True

        # 单个数字处理
        if len(s_input_val) == 1:
            return flag
        
        while left_index < right_index:
            if s_input_val[left_index] == s_input_val[right_index]:
                left_index = left_index + 1
                right_index = right_index - 1
            else:
                flag = False
                break

        return flag


if __name__ == "__main__":
    input_val = 1

    print(Solution.isPalindrome(input_val))