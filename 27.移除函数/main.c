/*
时间
    详情 0ms
    击败 100.00%使用 C 的用户
内存
    详情 6.40MB
    击败 12.25%使用 C 的用户
 */

#include <stdio.h>

int removeElement(int *nums, int numsSize, int val)
{
    int left_idx = 0;
    int right_idx = numsSize - 1;

    while (left_idx <= right_idx)
    {
        // 判断是否相等
        if (nums[left_idx] == val)
        {
            // 把右边的值覆盖左边。
            nums[left_idx] = nums[right_idx];
            // 便于观看，到时候右边全是-1.
            nums[right_idx] = -1;
            right_idx--;
        }
        // 不相等则左边的计数器加一
        else
        {
            left_idx++;
        }
    }

    return right_idx + 1;
}

int main()
{
    int nums[] = {};
    int val = 2;
    int num_size = sizeof(nums) / sizeof(int);

    int ret = removeElement(nums, num_size, val);
    printf("ret:%d\n", ret);

    int idx = 0;
    while (idx < num_size)
    {
        printf("%d ", nums[idx]);
        idx++;
    }

    return 0;
}