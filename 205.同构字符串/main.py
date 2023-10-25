
'''
解题思路：
    1.顺序遍历两个字符串。对A字符串的字符映射到数组A，同理B也是如此。
    2.同时判断映射后的数组数值是否相等。
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ret = True
        if len(s) != len(t):
            ret = False
            return ret
        s_arr = [0]*128
        t_arr = [0]*128
        gap = [256]*128
        for i in range(len(s)):
            # s字符串的ascii的数字
            s_idx = ord(s[i])
            t_idx = ord(t[i])
            s_arr[s_idx] += 1
            t_arr[t_idx] += 1
            # print("s_idx:", s_arr[s_idx], "t_idx:", t_arr[t_idx])

            # 判断方法一：两个数值不相等
            if s_arr[s_idx] != t_arr[t_idx]:
                ret = False
                break

            if gap[s_idx] == 256:
                # 获取两个ASCII的差值
                gap[s_idx] = s_idx - t_idx
            # 判断方法二：上下差值不相等
            elif gap[s_idx] != s_idx - t_idx:
                ret = False
                break

        return ret


if __name__ == "__main__":
    s = "bbbaaaba"
    t = "aaabbbba"

    solution = Solution()
    ret = solution.isIsomorphic(s, t)
    print("ret:", ret)
