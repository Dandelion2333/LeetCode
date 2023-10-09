/*
时间
    详情 28ms
    击败 92.07%使用 C 的用户
内存
    详情 10.76MB
    击败 20.75%使用 C 的用户

题目：
    给定一个含有 n 个正整数的数组和一个正整数 target 。

    找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
    并返回其长度。如果不存在符合条件的子数组，返回 0 。

    示例 1：
        输入：target = 7, nums = [2,3,1,2,4,3]
        输出：2
        解释：子数组 [4,3] 是该条件下的长度最小的子数组。

    示例 2：
        输入：target = 4, nums = [1,4,4]
        输出：1

    示例 3：
        输入：target = 11, nums = [1,1,1,1,1,1,1,1]
        输出：0

我的解题思路：
    从连续子序列入手。
    尽可能让子序列更段，从而满足题目的需求。
步骤：
    1.准备两个指针，分别为left与right，起始位置都是0
    2.left先出发向左移动，把路过的数据累加为sum。
    3.当sum等于target时，记录当前子序列数
    4.当sum大于target时，把sum减去right指针对应的数据。此处做while循环，
        4.1.sum小于target，执行步骤二
        4.2.sum等于target，执行步骤三
*/

#include <stdio.h>

int minSubArrayLen(int target, int *nums, int numsSize)
{
    int val = 0, tmp = 0;
    int right = 0, left = 0;
    int min = 100 * 1000 + 1;

    while (left < numsSize)
    {
        // 向右边累加
        val = val + nums[left];

        // 当相等的时候，记录当前子序列个数
        if (val == target)
        {
            tmp = left - right + 1;
            // 更新最小子序列个数
            if (tmp < min)
            {
                min = tmp;
            }
        }
        while (val >= target)
        {
            // 当大于的时候，记录当前子序列个数
            tmp = left - right + 1;
            // 更新最小子序列个数
            if (tmp < min)
            {
                min = tmp;
            }
            val = val - nums[right++];
        }

        left++;
    }

    // 没有匹配上的数据
    if (min == (100 * 1000 + 1))
    {
        min = 0;
    }

    return min;
}

int main()
{
    int nums[] = {2, 3, 1, 2, 4, 3};
    int val = 7;
    int num_size = sizeof(nums) / sizeof(int);

    int ret = minSubArrayLen(val, nums, num_size);
    printf("ret:%d\n", ret);

    // int idx = 0;
    // while (idx < num_size)
    // {
    //     printf("%d ", nums[idx]);
    //     idx++;
    // }

    return 0;
}