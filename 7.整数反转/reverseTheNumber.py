class Solution:
    def reverse(self, x):
        list = []
        # 判断数据的正负情况
        if x >= 0:
            signFlag = 0
        else:
            signFlag = 1
            x = x * (-1)

        # 转换成字符串处理
        string = str(x)

        # 反转数据
        lastNum = string[len(string)-1]
        rightCnt = len(string) - 1
        while rightCnt >=0:
            list.append(string[rightCnt])
            rightCnt = rightCnt - 1

        num = list[0]
        cnt = 1
        while cnt < (len(list)):
            num = num + list[cnt]
            cnt = cnt + 1
        
        # 把字符串转换为数字
        x = int(num)     

        # 还原符号
        if signFlag != 0:
            x = x * (-1)

        # 范围判断
        if x > 2147483647 or x < -2147483648:
            x = 0        
        
        return x

    def reverseTwo(self, x):
        cnt = 0
        signFlag = 0

        # 判断数据的正负情况
        if x >= 0:
            signFlag = 0
        else:
            signFlag = 1
            x = x * (-1)

        # 通过算法，把后面的数移到前面，每次移动一位
        while x != 0:
            cnt = cnt * 10 + int(x % 10)
            x = int(x / 10)

        # 还原符号
        if signFlag == 1:
            cnt = cnt * (-1)
        # 范围判断
        if cnt > 2147483647 or cnt < -2147483648:
            cnt = 0   

        return cnt



if __name__ == "__main__":
    num = -123

    num = Solution().reverseTwo(num)

    print(num)