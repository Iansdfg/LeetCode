# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def initList(arrary):
    if len(arrary) == 0:
        return None
    root = ListNode(arrary[0])
    result = root
    for index, value in enumerate(arrary):
        if index > 0:
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Recursive
        """
        if not (head and head.next):
            return head
        previous = current = ListNode(0)
        previous.next = head

        fast = current.next.next
        slow = current.next

        current.next = fast
        slow.next = fast.next
        fast.next = slow

        slow.next = self.swapPairs(current.next.next.next)

        return previous.next



        # if not (head and head.next):
        #     return False
        # previous = current = ListNode(0)
        # previous.next = head
        #
        # while current.next and current.next.next:
        #     fast = current.next.next
        #     slow = current.next
        #
        #     current.next = fast
        #     slow.next = fast.next
        #     fast.next = slow
        #
        #     current = current.next.next
        # return previous.next


def execute():
    l1 = initList([1,2,3])
    sol = Solution()
    printList(sol.swapPairs(l1))

if __name__ == '__main__':
    execute()

