class Solution():
    def mostPoint(self, points):
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        elif (len(points) == 2):
            return 2
        

        maxNum = Solution().poll(points)  

        if maxNum == len(points):
            maxNum = Solution().adjustMaxNum(points)

        return maxNum

    def adjustMaxNum(self, points):
        temp = points[1]
        points[1] = points[0]
        points[0] = temp
        
        maxNum = Solution().poll(points)

        return maxNum

    def poll(self, points):
        linePoint = []
        leftCnt = 0
        midCnt = 0
        rightCnt = 0
        maxNum = 0
        while leftCnt < len(points):
            linePoint = []
            midCnt = leftCnt + 1
            while midCnt < len(points):
                Solution().createLine(points[leftCnt][0], points[leftCnt][1], points[midCnt][0], points[midCnt][1], linePoint)                
                midCnt = midCnt +1
            # 获取本轮中直线最多的点的个数
            maxNumTemp = Solution().getMaxNum(linePoint)
            if maxNumTemp >= maxNum:
                maxNum = maxNumTemp
            leftCnt = leftCnt + 1
        
        return maxNum

    def createLine(self, x1, y1, x2, y2, linePoint):
        if (x1== x2) and (y1 == y2):
            k = 666666
            b = 666666
        else:
            if (x2 - x1) == 0:
                k = 999999
                b =  x1
            elif (y2 - y1) == 0:
                k = 0
                b = y1
            else:
                k = (float)(((y2 - y1) / (x2 - x1)))
                b = y1 - k * x1
        #print("k b", k, b, x1, y1, x2, y2)
        
        Solution().judgeKB(linePoint, k, b)

    def judgeKB(self, linePoint, k, b):

        cnt = 0
        while cnt < (len(linePoint)):
            if linePoint[cnt][1] == k and linePoint[cnt][2] == b and k != 666666 and b != 666666:
                linePoint[cnt][0] = linePoint[cnt][0] + 1
                #print("addvalue k b", k, b)
                break
            cnt = cnt + 1
        if cnt >= len(linePoint):
            linePoint.append([2, k, b])
            #print("append k b", k, b)            

    def getMaxNum(self, linePoint):
        maxNum = 0
        coincide = 0
        # 获取最大值
        for cnt in range (len(linePoint)):
            if linePoint[cnt][0] >= maxNum:
                maxNum = linePoint[cnt][0]
            if linePoint[cnt][1] == 666666 and linePoint[cnt][2] == 666666:
                coincide = coincide + 1

        if coincide == len(linePoint):
            # 表示数组中的点都是重合的
            return len(linePoint) + 1
        else:
            return (maxNum + coincide)


if __name__ == "__main__":
    points =  [[0,0],[0,0],[94911151,94911150],[94911152,94911151]]
    

    num = Solution().mostPoint(points)

    print(num)
