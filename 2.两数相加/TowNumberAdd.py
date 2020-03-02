class Solution:
    def addTwoNumbers(self, l1, l2):
        value1 = Solution().GenerateValue(l1)
        value2 = Solution().GenerateValue(l2)

        print(value1, value2)

        addValue = value1 + value2
        print(addValue)

        cnt = 10
        node = Node(int(addValue%cnt))
        list3  = List(node)
        addValue = int(addValue/10)
        while addValue > 0:
            node = Node(int(addValue%cnt))
            list3.addNode(node) 
            addValue = int(addValue / 10)

        val = Solution().GenerateValue(list3)
        print(val)


    def GenerateValue(self, ListNode):
        node = ListNode.val
        value = 0
        cnt = 1

        while node is not None:
            value = value + int(node.val)*cnt
            node = node.next
            cnt = cnt*10
        # print(value)
        return value

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class List:
    def __init__(self, node):
        self.val = node
        self.next = None

    def view(self):
        node = self.val
        linkStr = ''

        while node is not None:
            linkStr = linkStr + str(node.val)
            node = node.next

        #print(linkStr)

    def addNode(self, node):
        self.next = node
        self.next.next = None


if __name__ == "__main__":
    node1 = Node(4)
    node2 = Node(5)
    node3 = Node(3)
    node4 = Node(7)
    node5 = Node(3)

    list1 = List(node1)
    list1.addNode(node2)

    list2 = List(node4)
    list2.addNode(node5)

    Solution().addTwoNumbers(list1,list2)

