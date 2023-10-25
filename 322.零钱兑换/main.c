
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int coinChange(int *coins, int coinsSize, int amount)
{
    if (amount == 0)
    {
        return 0;
    }
    int num = 10 * 1000;
    char right = coinsSize - 1;
    char left;
    int tmp, new_amount;
    // 外层循环
    while (right >= 0)
    {
        // 新一轮数据更新
        left = right;
        new_amount = amount;
        tmp = 0;
        while (left >= 0)
        {
            // 判断amount与当前coins的最大值，
            if (new_amount - coins[left] >= 0)
            {
                new_amount -= coins[left];
                tmp++;
            }
            // 不满足则left向左移动
            else
            {
                left--;
            }
            // 退出循环
            if (new_amount == 0)
            {
                // 更新num
                if (tmp < num)
                {
                    printf("");
                    num = tmp;
                }
                break;
            }
        }
        right--;
    }
    // 没匹配上数据
    if (num == 10 * 1000)
    {
        num = -1;
    }
    return num;
}
int main()
{
    int coins[] = {186, 419, 83, 408};
    int coin_size = sizeof(coins) / sizeof(int);
    int amount = 6249;

    int num = coinChange(coins, coin_size, amount);
    printf("num:%d \n", num);
}