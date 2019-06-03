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
    count = 0
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        Recursive
        """
        # if not head: return head
        # next = self.removeNthFromEnd(head.next, n)
        # self.count += 1
        # if self.count == n:
        #     head = next
        # else:
        #     head.next = next
        # return head
        """
        Brutal
        """
        # i = 0
        # node = head
        # while node != None:
        #     i += 1
        #     node = node.next
        # target = i-n
        # print(target)
        # if target == 0:
        #     return head.next
        # else:
        #     node = head
        #     j = 0
        #     while node != None:
        #         if j == target-1:
        #             node.next = node.next.next
        #         else:
        #             node = node.next
        #         j += 1
        #     return head

        """
        Iterative
        """
        slow = fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast: return head.next # len == n
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


        # slow = fast = head
        # while n>0:
        #     fast = fast.next
        #     n -= 1
        # # print(fast.val)
        # prev = dummy = ListNode(-1)
        # dummy.next = head
        # while fast:
        #     prev = prev.next
        #     slow = slow.next
        #     fast = fast.next
        # # print(prev.val,slow.val)
        # prev.next = slow.next
        # return dummy.next


def execute():
    l1 = initList([1,2,3,4,5])
    n = 5
    sol = Solution()
    head = l1
    printList(sol.removeNthFromEnd(head, n))

if __name__ == '__main__':
    execute()

