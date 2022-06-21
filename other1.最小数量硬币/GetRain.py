

class Solution:
    def get_min_num(self, coins, amount):
        min_num = 0

        coins.sort()
        print(coins)
        
        num = len(coins)
        cnt = num -1

        # 从数组的最大值开始遍历
        # print("采用的面值如下:")
        while cnt >= 0:
            if coins[cnt] <= amount:
                # print(coins[cnt])
                amount = amount - coins[cnt]
                min_num += 1
            else:
                cnt -= 1        
                
        if amount != 0:
            # print("无正常与之匹配的面额")
            min_num = -1

        return min_num


if __name__ == "__main__":
    list = [186,419,83,408]
    value = 6249
    min_num = Solution().get_min_num(list, value)
    
    print("最少需要:",min_num)