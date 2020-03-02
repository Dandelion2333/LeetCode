def ShellSort(ShMatrix):
    gap = int((len(ShMatrix) / 2))
    
    while gap > 0:
        begin = 0
        # Set each data loop
        while begin < gap:
            rightCnt = begin + gap

            # Sorting of each group of data after separation by gaps
            while rightCnt < len(ShMatrix):
                if ShMatrix[rightCnt] < ShMatrix[rightCnt - gap]:
                    leftCnt = rightCnt - gap
                    insertValue = ShMatrix[rightCnt]
                    while leftCnt > (begin - gap) and ShMatrix[leftCnt] > insertValue:
                        ShMatrix[leftCnt + gap] = ShMatrix[leftCnt]
                        leftCnt = leftCnt - gap
                    ShMatrix[leftCnt + gap] = insertValue

                rightCnt = rightCnt + gap
            begin = begin + 1
        gap = int((gap / 2))

    return ShMatrix

if __name__ == "__main__":
    s = "a"
    t = "b"

    print(len(s))

    sList = []
    tList = []

    if len(sList) != len(tList):
        result = False    
    else:
        # 把字符串转换成数字，并存入list
        for ch in s:
            sList.append(ord(ch))

        for ch in t:
            tList.append(ord(ch))

        sList = ShellSort(sList)
        tlist = ShellSort(tList)

        result = 1
        cnt  = 0
        # 判断两个排好序之后的list是否全等
        while cnt < len(sList):
            if sList[cnt] != tList[cnt]:
                print("false")
                result = 0
                break
            cnt = cnt + 1


    print("result:%d" % result)
        
