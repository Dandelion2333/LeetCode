/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 * C语言解答版本
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    int value1[100] = {0};
    int value2[100] = {0};
    int value3[100] = {0};
    int length1 = -1, length2 = -1, length3 = 0, cnt = 0;
    int flag = 0;

    struct ListNode *tail;
    struct ListNode *l3, *l4;
    // 数据的低位在数组的低位
    while (l1 != NULL)
    {
        value1[++length1] = l1->val;
        l1 = l1->next;
    }

    while (l2 != NULL)
    {
        value2[++length2] = l2->val;
        l2 = l2->next;
    }

    while(cnt <= length1 || cnt <= length2 || flag == 1)
    {
        // 假如两个数相加大于9，则需要进一
        if(value1[cnt] + value2[cnt] + flag > 9)
        {
            value3[cnt] = value1[cnt] + value2[cnt] - 10 + flag;
            flag = 1;
        }
        else
        {
            value3[cnt] = value1[cnt] + value2[cnt] + flag;
            flag = 0;
        }
        cnt++;
    }

    l3 = (struct ListNode*)malloc(sizeof(struct ListNode));
    l3->val = value3[length3++];
    l3->next = NULL;
    tail = l3;
    while (length3 < cnt)
    {
        l4 = (struct ListNode*)malloc(sizeof(struct ListNode));
        l4->val = value3[length3++];
        l4->next = NULL;
        tail->next = l4;
        tail = l4;
    }

    return l3;
}