# 实现方法：
#   采用常规逻辑，遍历字符串，然后判断与处理字符
#   与上一个版本的区别在于，逻辑比较清晰，一气呵成。
#   具体思路如下：
#       1、首个非空格字符之前的处理。采用过滤的方式。
#       2、首个非空格字符自身的处理。判断其类型。是符号位，还是数字，还是无用字符
#       3、首个非空格字符之后的处理。除数字之外的所有字符都去除。即直接break
#       4、遍历结束之后，加上符号位与限定最大最小值。
# 
#   优势:
#       1、一定程度上提高了执行速度。
#   劣势：
#       2、空间复杂度没有任何变化。因为实现的底层逻辑没有改变。


class Solution:
    def my_atoi(self, input_string):
        # 用于确定输出数字的符号，0为未知，1为正，2为负
        symbol_val = 0
        
        output_value = ""
        blank_flag = False
        symbol_flag = False
        
        # 遍历输入字符串
        for cnt in range(len(input_string)):
            # print("string:", val)
            val = input_string[cnt]
            
            # 过滤掉首个非空格字符之前的空格-例如"   12 3"，则过滤点1之前的空格
            if blank_flag == False:
                if Solution().is_blank(val) == True:
                    continue
                else:
                    blank_flag = True
            
            # 判断首个非空格字符是否为符号位
            if symbol_flag == False:
                symbol_val = Solution().is_symbol(val)
                # 非符号位
                if symbol_val == 0:
                    if Solution().is_num(val) == True:
                        # 是数字，则记录数字
                        output_value = output_value + val
                        # 此时，默认符号是正
                        symbol_flag = True
                        symbol_val = 1
                        # 此时，空格也算是多余的干扰字符
                        blank_flag = True
                    else:
                        # 不是数字，也不是符号位，则直接给0并且break
                        output_value = "0"
                        break
                else:
                    symbol_flag = True
                    # 此时，空格也算是多余的干扰字符
                    blank_flag = True
                    
                # 首个字符判断完之后，后面的等下一轮处理
                continue
            
            # 后续字符的处理
            if Solution().is_symbol(val) == 0 and Solution().is_num(val) == True and Solution().is_blank(val) == False:
                output_value = output_value + val
            else:
                break
        
        # 特殊处理，当一个数字也没有的情况
        if output_value == "":
            output_value = 0
            # 清除符号位
            symbol_val = 0

        # 添加符号位置
        if symbol_val == 2:
            output_value = "-" + output_value
            
        # 判断是否超出范围
        min = -2147483648
        max = 2147483647
        # output_value = "-2147483649"
        new_value = int(output_value) 
        # print("new_value:", new_value)
        
        if new_value < min:
            new_value = min
        if new_value > max:
            new_value = max
        return new_value

    # 判断是否为数字
    def is_num(self, value):
        if value == "0" or value == "1" or value == "2" or value == "3" or value == "4" \
        or value == "5" or value == "6" or value == "7" or value == "8" or value == "9":
            return True
        else:
            return False
        
    # 判断是否为符号
    def is_symbol(self, value):
        if value == "+":
            return 1
        elif value == "-":
            return 2
        else:
            return 0
        
    # 判断是否为空格
    def is_blank(self, value):
        if value == " ":
            return True
        else:
            return False
        
if __name__ == "__main__":
    num = "- 41 3"
    num = Solution().my_atoi(num)

    print(num)