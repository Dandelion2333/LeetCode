"""
题目：
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

    有效字符串需满足：

    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。

解题思路：
    定义一个栈模型，通过压入与弹出方式解决
    问题1：可以用python的栈模块吗，还是要自己手写栈

进度：
    python：已经完成
    C++：还未开始

执行结果：
    未记录
"""

class Solution1:
    def isValid(s: str) -> bool:
        flag = True
        str_len = len(s)
        str_stack = []

        for cnt in range(str_len):
            val = s[cnt]
            if val == '(' or val == '[' or val == '{':
                Solution1.input_stack(str_stack, val)

            if val == ')':
                pop_val = Solution1.output_stack(str_stack)
                if pop_val == '(':
                    flag = True
                else:
                    flag = False
                    return flag

            if val == ']':
                pop_val = Solution1.output_stack(str_stack)
                if pop_val == '[':
                    flag = True
                else:
                    flag = False
                    return flag

            if val == '}':
                pop_val = Solution1.output_stack(str_stack)
                if pop_val == '{':
                    flag = True
                else:
                    flag = False
                    return flag

        # 判断栈是否为空
        if len(str_stack) != 0:
            flag = False

        return flag

    # 入栈
    def input_stack(str_stack, val):
        str_stack.insert(0, val)

    def output_stack(str_stack):
        # 删除栈顶元素
        if len(str_stack) >= 1:
            return str_stack.pop(0)
        else:
            # 假如返回0，那么一定匹配不上
            return 0

    # 打印栈元素
    def print_stack(str_stack):
        for cnt in range(len(str_stack)):
            print(str_stack[cnt])

if __name__ == "__main__":
    input_string = "[(({})}]"

    print(Solution1.isValid(input_string))