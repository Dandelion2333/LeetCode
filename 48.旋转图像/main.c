/*
时间
    0 ms 击败 100%
内存
    6.8 MB 击败 19.80%

我的解题思路
    1.根据翻转之后的坐标规律得出一个公式。因为翻转之后的位置是固定的。
    2.中间遇到的原数据被覆盖的问题。我想的办法是记录原数据与被覆盖位置的数据，然后循环处理一圈，再继续处理下一圈。
        看一下别人是如何解决被覆盖的问题。
我的耗时
    1.没有把输入数据的格式弄清楚，所以一个简单的公式，调试了很久，浪费了很多时间。
    2.没有把输入数据的坐标与本地计算公式的坐标映射正确。不是自己想当然的弄一个坐标系。而是要根据输入的二维数组来定。
经验积累
    1.先看清楚题目的输入与输出。不要急着立马就做题。万一搞错了输入或者输出会浪费很多时间。

别人的解决方案
    1.常规思路上我与官方是一样的
    2.解决覆盖的问题。
        它是一次性把四个变量都替换了。这样就不用最里层的while(1)循环了。理解原理后可读性更高，更好理解一点。是我该优化的点。
    3.使用水平翻转+对角线翻转解决。
        这个方法很聪明啊，感觉翻转的问题都可以使用这个方法。好理解，好实现。
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void rotate(int **matrix, int matrixSize, int *matrixColSize)
{
    int after_x = 0, after_y = 0;
    int before_x = 0, before_y = 0;
    int before_tmp = 0, cover_tmp = 0;
    int ex_cnt = 0;

    // 一层一层的处理处理，速度会非常的快。总体时间小于O(n)
    while (ex_cnt < matrixSize / 2)
    {
        // 获取下一层的起始位置
        before_x = ex_cnt;
        before_y = ex_cnt;

        // 遍历到x坐标的倒数第二个数据。
        while (before_x < matrixSize - 1 - ex_cnt)
        {
            int break_x = before_x;
            int break_y = before_y;
            // 记录之前的数据
            before_tmp = matrix[before_x][before_y];

            // 处理当前层的数据，while里面填写1也可以。因为y肯定在matrixSize之内，不会超出这个边界
            while (1)
            {
                // 转换后的x轴等于偏移量-之前的y
                after_x = before_y;
                // y轴的数据保持不变
                after_y = matrixSize - 1 - before_x;

                // 记录被覆盖之前的数据
                cover_tmp = matrix[after_x][after_y];

                // 更新数据
                matrix[after_x][after_y] = before_tmp;

                // 更新
                before_tmp = cover_tmp;

                // 更新坐标
                before_x = after_x;
                before_y = after_y;

                // 到达起始位置，退出循环
                if (before_x == break_x && before_y == break_y)
                {
                    break;
                }
            }
            before_x++;
        }
        ex_cnt++;
    }
}

int main()
{
#define value 5
    int matrix[value][value] = {{5, 1, 9, 11, 1}, {2, 4, 8, 10, 1}, {13, 3, 6, 7, 1}, {
                                                                                          15,
                                                                                          14,
                                                                                          12,
                                                                                          16,
                                                                                      },
                                {1, 1, 1, 1, 1}};
    // int matrix[value][value] = {{1, 2}, {3, 4}};
    int test = value;
    int *matrixColSize = &test;
    int *p = &matrix[0][0];
    // int **pp = &p;

    int idx = 0;
    while (idx < value)
    {
        int cnt = 0;
        while (cnt < value)
        {
            printf("%d ", matrix[idx][cnt]);
            cnt++;
        }
        printf("\n");
        idx++;
    }
    rotate(&p, value, matrixColSize);

    idx = 0;
    while (idx < value)
    {
        int cnt = 0;
        while (cnt < value)
        {
            printf("%d ", matrix[idx][cnt]);
            cnt++;
        }
        printf("\n");
        idx++;
    }

    return 0;
}