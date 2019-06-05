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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next: return head
        #
        # result = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return result

        # if node == None:
        #     return None
        # if node.next == None:
        #     return node
        # result = self.reverseList(node.next)
        # node.next.next = node
        # node.next = None
        # return result


        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


def execute():
    l1 = initList([1,2,3,4,5])
    sol = Solution()
    printList(sol.reverseList(l1))

if __name__ == '__main__':
    execute()

