

class Solution:
    def maxArea(self, height):
        flag = 0
        leftCnt = 0
        rainArea = 0
        allArea = 0
        pillarArea = 0
        secondaryVal = 0
        secondaryCnt = 0

        # 柱子构成的面积
        for cnt in range (len(height)):
            pillarArea = pillarArea + height[cnt]


        # 获取构成最大的面积
        while leftCnt < len(height):
            rightCnt = leftCnt + 1
            #print(rightCnt)

            while rightCnt < len(height):
                if height[rightCnt] < height[leftCnt]:
                    # 找出第二大的数
                    if secondaryVal <= height[rightCnt]:
                        secondaryVal = height[rightCnt]
                        secondaryCnt = rightCnt

                    rightCnt = rightCnt + 1
                    flag = 1
                else:
                    flag = 2
                    break
            # when not number than height[leftCnt] big
            if flag == 1:
                allArea = allArea + height[leftCnt] + (secondaryCnt - leftCnt - 1) * height[secondaryCnt]
                print("a", leftCnt, secondaryCnt, allArea)
                leftCnt = secondaryCnt
                flag = 0
            elif flag == 2:
                allArea = allArea + (rightCnt - leftCnt) * height[leftCnt]
                print("b", leftCnt, rightCnt, allArea)
                # update the letfcnt
                leftCnt = rightCnt
                flag = 0
            else:
                allArea = allArea + height[leftCnt]
                print("c", leftCnt, leftCnt, allArea)
                leftCnt = leftCnt + 1
            
            secondaryVal = 0
            secondaryCnt = 0

        print(allArea, pillarArea)
        rainArea = allArea - pillarArea
        
        return rainArea


if __name__ == "__main__":
    list = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
    #list = [0,1,0]
    num = Solution().maxArea(list)
    
    print(num)