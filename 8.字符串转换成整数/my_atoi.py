# 实现方法：
#   逻辑很常规，遍历字符串，然后一个一个的判定。
#   缺点：太多的特殊处理（打了各种补丁），显得很混乱


class Solution:
    def my_atoi(self, input_string):
        # 用于确定输出数字的符号，0为未知，1为正，2为负
        string_symbol = 0
        # 保存输出数值
        output_value = "0"
        
        # 定位首个非空字符
        flag = False

        # 遍历输入字符串
        for cnt in range(len(input_string)):
            # print("string:", val)
            val = input_string[cnt]
            
            # 去除空格
            if Solution().is_blank(val) == True and flag == False:
                continue
            
            # 判断首个字符是否为非数字，符号，空格
            if flag == False and Solution().is_num(val) == False and Solution().is_symbol(val) == 0:
                output_value = "0"
                flag = True
                break
            
            # 判断符号位
            if string_symbol == 0:
                # 从符号判定
                string_symbol = Solution().is_symbol(val)
                if string_symbol != 0:
                    flag = True
                
                # 从数字判定
                if Solution().is_num(val) == True:
                    string_symbol = 1
                    output_value = output_value + val
                    flag = True
            else:
                if Solution().is_symbol(val) == 0 and Solution().is_num(val) == True and Solution().is_blank(val) == False:
                    output_value = output_value + val
                    flag = True
                else:
                    break

        # 添加符号位置
        if string_symbol == 2:
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
    num = "+ 413"
    num = Solution().my_atoi(num)

    print(num)