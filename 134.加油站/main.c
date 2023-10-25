/*
时间
    详情 168ms
    击败 27.08% 使用 C 的用户
内存
    详情 14.51MB
    击败 6.30% 使用 C 的用户

我的解题思路还需要优化。
    理论上是很好的。只需要O(n)，但在执行的过程中重复过多了。
 */

#include <stdio.h>

int canCompleteCircuit(int *gas, int gasSize, int *cost, int costSize)
{
    // 第一个加油站的下标
    int first = -1;

    // 入口参数检查
    if (gasSize != costSize)
    {
        return first;
    }

    // 特殊情况处理
    if (gasSize == 1)
    {
        if (gas[0] >= cost[0])
        {
            return 0;
        }
        else
        {
            return -1;
        }
    }

    int idx = 0, flag = 0;
    int sum_gas = 0, sum_cost = 0;
    int cnt = 0;
    while (1)
    {
        idx = cnt % costSize;

        // 当回到第一个加油站的位置时，退出循环
        if (idx == first)
        {
            // 没有找到加油站
            if (flag == 0)
            {
                first = -1;
            }
            break;
        }
        // 最多允许执行完第二遍
        if ((cnt / costSize) >= 2)
        {
            // 没有找到加油站
            first = -1;
            break;
        }
        // 寻找到第一个够油的加油站
        if (flag == 1)
        {
            // 获取油与路径
            sum_gas += gas[idx];
            sum_cost += cost[idx];
            // printf("idx:%d sum_gas:%d sum_cos:%d\n", idx, sum_gas, sum_cost);

            // 油不够
            if (sum_gas < sum_cost)
            {
                // 需要重新寻找加油站
                flag = 0;
                // 清空数据
                sum_gas = 0;
                sum_cost = 0;
            }
        }
        else
        {
            // 寻找成功
            if (gas[idx] >= cost[idx])
            {
                first = idx;
                flag = 1;
                // 获取当前加油站的油
                sum_gas = gas[idx];
                // 获取从当前加油站出发，到下个加油站的距离
                sum_cost = cost[idx];
            }
        }

        cnt++;
    }

    // 返回的是数组下标
    return first;
}

int main()
{
    int gas[] = {5, 0, 9, 4, 3, 3, 9, 9, 1, 2};
    int cost[] = {6, 7, 5, 9, 5, 8, 7, 1, 10, 5};
    int gasSize = sizeof(cost) / sizeof(int);
    int costSize = sizeof(cost) / sizeof(int);

    int ret = canCompleteCircuit(gas, gasSize, cost, costSize);
    printf("ret:%d\n", ret);

    // int idx = 0;
    // while (idx < num_size)
    // {
    //     printf("%d ", nums[idx]);
    //     idx++;
    // }

    return 0;
}