/*
时间
    0 ms 击败 100%
内存
    6.8 MB 击败 19.80%

我的解题思路
    1.

别人的解决方案
    1.


备注：
    C语言处理这类字符很不方便。
    所以用Python来做吧
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

// 链表节点结构
struct Node
{
    char data[4];
    struct Node *next;
};

// 队列结构
struct Queue
{
    struct Node *front;
    struct Node *rear;
};

// 创建一个空队列
struct Queue *createQueue()
{
    struct Queue *queue = (struct Queue *)malloc(sizeof(struct Queue));
    if (!queue)
    {
        perror("Memory allocation error");
        exit(1);
    }
    queue->front = queue->rear = NULL;
    return queue;
}

// 检查队列是否为空
int isEmpty(struct Queue *queue)
{
    return (queue->front == NULL);
}

// 入队操作
void enqueue(struct Queue *queue, char *item)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    if (!newNode)
    {
        perror("Memory allocation error");
        exit(1);
    }
    printf("data:%s len:%d\n", newNode->data, strlen(item));
    memcpy(newNode->data, item, strlen(item));
    newNode->next = NULL;

    if (isEmpty(queue))
    {
        queue->front = queue->rear = newNode;
    }
    else
    {
        queue->rear->next = newNode;
        queue->rear = newNode;
    }
}

// 出队操作
char *dequeue(struct Queue *queue)
{
    if (isEmpty(queue))
    {
        printf("Queue is empty. Cannot dequeue.\n");
        return NULL;
    }
    char *item = queue->front->data;
    struct Node *temp = queue->front;

    if (queue->front == queue->rear)
    {
        queue->front = queue->rear = NULL;
    }
    else
    {
        queue->front = queue->front->next;
    }

    free(temp);
    return item;
}

char phone[10][5] = {"\0", "\0", "abc\0", "def\0", "ghi\0"};
char **value = NULL;
// 回溯完成后获取到string
char string[4] = {0};

char **letterCombinations_new(char *digits, int *returnSize)
{
    struct Queue *queue = createQueue();

    int size = 32;
    value = (char **)malloc(size * sizeof(char *));
    int digits_len = strlen(digits);
    int str_cnt = 0, str_num = 0, idx = 0;

    // 把初始化的数据入队列
    str_num = digits[0] - '0';
    // 把字符数据入队
    str_cnt = 0;
    while (str_cnt < str_num)
    {
        string[0] = phone[str_num][str_cnt];
        string[1] = '\0';
        printf("str_num:%d phone:%c string:%s \n", str_num, phone[str_num][str_cnt], string);
        enqueue(queue, string);
        str_cnt++;
    }

    // int cnt = 0;
    // while (cnt < digits_len)
    // {
    //     str_num = atoi(digits[cnt]);
    //     // 把字符数据入队
    //     str_cnt = 0;
    //     while (str_cnt < str_num)
    //     {
    //         enqueue(queue, phone[cnt][str_cnt]);
    //         str_cnt++;
    //     }
    // }

    idx = 0;
    while (idx < size)
    {
        char *de_string = dequeue(queue);
        if (de_string == NULL)
        {
            break;
        }
        value[idx] = (char *)malloc(sizeof(de_string));
        memcpy(value[idx], de_string, sizeof(de_string));
    }

    *returnSize = size;

    return value;
}

int main()
{
    char digits[] = "23";
    int size = 0;
    int *returnSize = &size;

    char **value = letterCombinations_new(digits, returnSize);
    int idx = 0;
    while (idx < size)
    {
        printf("value2:%s ptr:%p\n", value[idx], value[idx]);
        idx++;
    }

    return 0;
}