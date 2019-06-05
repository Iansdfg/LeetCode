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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = head = ListNode(0)

        while l1 and l2:
            if l1.val > l2.val:
                current.next = l2
                l2 = l2.next
            else:
                current.next = l1
                l1 = l1.next
            current = current.next
        current.next = l1 or l2
        return head.next
        # if l1 == None:
        #     return l2
        # if l2 == None:
        #     return l1
        # if l1 == None and l2 == None:
        #     return None
        # array = []
        # while l1 != None and l2 != None:
        #     if l1.val < l2.val:
        #         array.append(l1.val)
        #         l1 = l1.next
        #     else:
        #         array.append(l2.val)
        #         l2 = l2.next
        # while l1 != None:
        #     array.append(l1.val)
        #     l1 = l1.next
        # while l2 != None:
        #     array.append(l2.val)
        #     l2 = l2.next
        # # print(array)
        # if len(array) > 0:
        #     root = ListNode(array[0])
        #     result = root
        #     for index, value in enumerate(array):
        #         if index > 0:
        #             root.next = ListNode(value)
        #             root = root.next
        # return result



def execute():
    l1 = initList([1,3,4])
    l2 = initList([1,2,4])
    sol = Solution()
    printList(sol.mergeTwoLists(l1, l2))

if __name__ == '__main__':
    execute()

