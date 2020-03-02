class Solution:
    def maxPoints(self, points):
        points, deleteNum = Solution.RemoveDuplicateElements(points)

        kList = []
        pList = []
        disposeList = []
        if len(points) > 1:
            for leftCnt in range (len(points)):
                rightCnt = leftCnt + 1
                while rightCnt < (len(points)):
                    k = Solution.GetSlope(points[leftCnt][0], points[leftCnt][1], points[rightCnt][0], points[rightCnt][1])
                    kList.append(k)
                    pList.append(points[leftCnt])

                    disposeList = Solution.DisposeK(k, points[leftCnt][0], points[leftCnt][1], disposeList)

                    rightCnt = rightCnt + 1
            
            print("len(klist)",len(kList))
            print(kList)
            print(len(pList))
            print(pList)
            print("disposeList",disposeList)
            kCount = Solution.GetKCount(disposeList)
            # print(kCount)
            # #print(max(kList, key=kList.count))
            # kCount = kList.count(max(kList, key=kList.count))
            print(kCount, kList)
            kNum = Solution.GetKNum(kCount)
            # #print(kCount, kNum, kList)
        else:
            if len(points) == 0:
                kNum = 0
            elif len(points) == 1:
                kNum = 1

        return (kNum + deleteNum)

    def GetKCount(disposeList):
        kCount = 0
        
        for cnt in range (len(disposeList)):
            if kCount < (disposeList[cnt][2]):
                kCount = disposeList[cnt][2]
            
        return kCount

    def DisposeK(k, x, y, disposeList):
        flag = False
        if k == 999999:
            b = x
        else:
            b = round((y - k*x), 6)

        for index in range (len(disposeList)):
            if (k == disposeList[index][0]) and (b == disposeList[index][1]):
                flag = True
                disposeList[index][2] = disposeList[index][2] + 1

        if flag == False:        
            num = 1
            disposeList.append([k, b, num])
        
        return disposeList

    def GetSlope(x1, y1, x2, y2):
        if (x2 - x1) != 0:
            k = (((y2 - y1) / (x2 - x1)))
        else:
            k = 999999

        return k
    def GetKNum(kCount):
        kNum = 0
        while 1:
            if (kNum * kNum - kNum) >= (kCount*2):
                print(kNum)
                break
            
            kNum = kNum + 1
        return kNum
    def RemoveDuplicateElements(list):
        deleteNum = 0
        for leftCnt in range (len(list)):
            rightCnt = leftCnt + 1
            while rightCnt < len(list):
                if (list[leftCnt][0] == list[rightCnt][0]) and (list[leftCnt][1] == list[rightCnt][1]):
                    del list[rightCnt]
                    deleteNum = deleteNum + 1
                rightCnt = rightCnt + 1
        print(deleteNum)
        return list, deleteNum

if __name__ == "__main__":
    list = [[-435,-347],[-435,-347],[609,613],[-348,-267],[-174,-107],[87,133],[-87,-27],[-609,-507],[435,453],[-870,-747],[-783,-667],[0,53],[-174,-107],[783,773],[-261,-187],[-609,-507],[-261,-187],[-87,-27],[87,133],[783,773],[-783,-667],[-609,-507],[-435,-347],[783,773],[-870,-747],[87,133],[87,133],[870,853],[696,693],[0,53],[174,213],[-783,-667],[-609,-507],[261,293],[435,453],[261,293],[435,453]]
    result = Solution().maxPoints(list)

    print(result)

