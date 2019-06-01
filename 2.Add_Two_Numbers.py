# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def initList(arrary):
    root = ListNode(arrary[0])
    result = root
    for index, value in enumerate(arrary):
        if index>0:
            root.next = ListNode(value)
            root = root.next
    return result

def printList(linkedlist):
    if linkedlist:
        print('[', end = '')
        while linkedlist.next:
            print(linkedlist.val, end = ', ')
            linkedlist = linkedlist.next
        print(linkedlist.val, end = ']\n')
    else:
        print('[]')


class Solution(object):
    def addTwoNumbers1(self, l1, l2, carry):
        if not l1 and not l2 and carry == 0: return None
        result = ListNode(0)
        val = carry
        if l1:
            val += l1.val
        if l2:
            val += l2.val
        result.val = val % 10
        if l1 or l2:
            next = self.addTwoNumbers1(l1.next if l1.next else None, l2.next if l2.next else None, 1 if val >= 10 else 0)
            result.next = next
        return result

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        recursive
        """
        return self.addTwoNumbers1(l1, l2, 0)

        """
        iterative
        """
        # carry = 0
        # head = curr = ListNode(-1)
        # while l2 or l1 or carry == 1:
        #     val = carry
        #     if l1:
        #         val += l1.val
        #         l1 = l1.next
        #     if l2:
        #         val += l2.val
        #         l2 = l2.next
        #     curr.next = ListNode(val % 10)
        #     carry = int(val/10)
        #     curr = curr.next
        # return head.next

def execute():
    l1 = initList([2,4,6])
    l2 = initList([5,6,4])
    sol = Solution()
    printList(sol.addTwoNumbers(l1, l2))

if __name__ == '__main__':
    execute()

