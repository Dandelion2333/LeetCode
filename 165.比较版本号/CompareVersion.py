
class Solution:
    def CompareVersion(self, version1, version2):
        list1 = []
        list2 = []
        value1 = 0
        value2 = 0

        for cnt1 in range (len(version1)):
            if version1[cnt1] != '.':
                value1 = (value1 * 10) + int(version1[cnt1])
            else:
                list1.append(value1)
                value1 = 0
            # 把最后一个点之后的数据加入到队列中
            if cnt1 == len(version1) - 1:
                list1.append(value1)

        for cnt2 in range (len(version2)):
            if version2[cnt2] != '.':
                value2 = (value2 * 10) + int(version2[cnt2])
            else:
                list2.append(value2)
                value2 = 0
            # 把最后一个点之后的数据加入到队列中
            if cnt2 == len(version2) - 1:
                list2.append(value2)
                
        # print(list1)
        # print(list2)
        
        # 最高版本最大的情况
        num = Solution().ListCompare(list1, list2)

        return num


    def ListCompare(self, list1, list2):
        # 把两个list补齐，使之个数相同
        list1, list2 = Solution().MakeupList(list1, list2)

        # print(list1, list2)
        for cnt in range (len(list1)):
            if list1[cnt] > list2[cnt]:
                return 1
            elif list1[cnt] < list2[cnt]:
                return -1
            else:
                num = 0

        return num

    def MakeupList(self, list1, list2):
        if len(list1) > len(list2):
            cnt = len(list2)
            while cnt < len(list1):
                list2.append(0)
                cnt = cnt + 1
        else:
            cnt = len(list1)
            while cnt < len(list2):
                list1.append(0)
                cnt = cnt + 1

        return list1, list2

if __name__ == "__main__":
    str1 = "1.0"
    str2 = "1.0.0"

    num = Solution().CompareVersion(str1 ,str2)
    
    print(num)

    