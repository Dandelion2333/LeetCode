

class Solution:
    def findContinuousSequence(self, target):
        list = []
        list.append(Solution().twoNum(target))


        return list

    def twoNum(self, target):
        list = []
        maxValue = int(target/2) + 1
        initVal = 1
        
        while initVal < maxValue:
            maxNumber = int(target/2) + 1
            #print(initVal, maxNumber)
            while maxNumber > 0:
                
                if Solution().Cumulative(initVal, maxNumber) == target:
                    tempVal = initVal
                    newCnt = 0
                    
                    while newCnt < maxNumber:
                        
                        list.append(tempVal)
                        tempVal = tempVal + 1
                        newCnt = newCnt + 1
                    # 相同个数的连续数据，只有一组满足条件
                    break
                
                maxNumber = maxNumber - 1
            initVal = initVal +  1
            
        return list

    def Cumulative(self, value, number):
        addCum = 0
        newCnt = 0
        while newCnt < number:
            addCum = addCum + value
            value = value + 1
            newCnt = newCnt + 1
        return addCum

if __name__ == "__main__":
    target = 15

    list = Solution().findContinuousSequence(target)

    print(list)
