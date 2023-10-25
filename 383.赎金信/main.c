/*
时间

内存


我的解题思路

 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool canConstruct(char *ransomNote, char *magazine)
{
    bool ret = true;

    // 创建哈希表
    int hash[26] = {0};

    int r_size = strlen(ransomNote);
    int m_size = strlen(magazine);

    int idx = 0;
    bool r_flag = false;
    bool m_flag = false;
    // 遍历ransomNote，记录每个字符出现的次数
    while (1)
    {
        if (idx < r_size)
        {
            // 把ransomNote的字符映射到数组的下标，做一个哈希映射
            hash[ransomNote[idx] - 'a'] -= 1;
        }
        else
        {
            // 完成
            r_flag = true;
        }
        if (idx < m_size)
        {
            // 把magazine的字符映射到数组的下标，做一个哈希映射，与ronsomNote的数据相减。目的是判断该字符是否重合。
            hash[magazine[idx] - 'a'] += 1;
        }
        else
        {
            // 完成
            m_flag = true;
        }
        // 同时完成则退出
        if (r_flag && m_flag)
        {
            break;
        }

        idx++;
    }

    idx = 0;
    while (idx < 26)
    {
        if (hash[idx] < 0)
        {
            ret = false;
            break;
        }
        idx++;
    }

    return ret;
}

int main()
{
    // int gas[] = {5, 0, 9, 4, 3, 3, 9, 9, 1, 2};
    // int cost[] = {6, 7, 5, 9, 5, 8, 7, 1, 10, 5};
    // int gasSize = sizeof(cost) / sizeof(int);
    // int costSize = sizeof(cost) / sizeof(int);

    char ransomNote[] = "bg";
    char magazine[] = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj";
    int ret = canConstruct(ransomNote, magazine);
    printf("ret:%d\n", ret);

    // int idx = 0;
    // while (idx < num_size)
    // {
    //     printf("%d ", nums[idx]);
    //     idx++;
    // }

    return 0;
}