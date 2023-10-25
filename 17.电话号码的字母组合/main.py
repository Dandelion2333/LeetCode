
phone = {}
phone['2'] = "abc"
phone['3'] = "def"
phone['4'] = "gji"


def back(in_put, string):
    out_put = []
    for ex_cnt in range(len(in_put)):
        for in_cnt in range(len(string)):
            out_put.append(in_put[ex_cnt] + string[in_cnt])
    return out_put


def letterCombinations(digits):

    # 输出字符串
    out_put = []
    string = phone[digits[0]]
    for cnt in range(len(string)):
        out_put.append(string[cnt])

    for cnt in range(1, len(digits)):
        out_put = back(out_put, phone[digits[cnt]])

    return out_put


if __name__ == "__main__":

    digits = "234"
    out_put = letterCombinations(digits)

    print(out_put)
