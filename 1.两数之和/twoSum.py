

class Solution_hash:
    def twoSum(self, nums, target):
        #  创建字典，也就是哈希表
        hashtable = dict()

        # 循环遍历nums
        for cnt, value in enumerate(nums):
            # print("cnt:", cnt, "value:", value)
            # 判断 target-value 否在在哈希表的key里面
            if target-value in hashtable:
                # value存储的是数组下标，所以直接由key找到。
                # 因为target = A + B . 此时，target-value为A，value为B。
                return [hashtable[target-value], cnt]
            else:
                # 把数组的元素作为key，数组的下标作为value存到哈希表中
                hashtable[value] = cnt

        return []

if __name__ == "__main__":
    nums = [2,11,15,7]
    target = 9
    result = Solution_hash().twoSum(nums, target)

    print("result:", result)