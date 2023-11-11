from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list(self) -> list:
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result

    def __repr__(self) -> str:
        return str(self.to_list())


class Solution:
    # def duplicateList(self, list):
    #     curr = list
    #     head = None
    #     prev = None
    #     while curr:
    #         if not head:
    #             head = ListNode(curr.val)
    #             prev = head
    #             curr = curr.next
    #             continue
    #
    #         n = ListNode(curr.val)
    #         prev.next = n
    #         prev = n
    #         curr = curr.next
    #
    #     return head

    # refactor
    # def duplicateList(self, list):
    #     curr = list
    #     head = ListNode(curr.val)
    #     prev = head
    #     curr = curr.next
    #
    #     while curr:
    #         n = ListNode(curr.val)
    #         prev.next = n
    #         prev = n
    #         curr = curr.next
    #
    #     return head

    # simplified
    def duplicateList(self, l):
        dummy = ListNode()
        tail = dummy

        while l:
            n = ListNode(l.val)
            tail.next = n
            tail = n
            l = l.next

        return dummy.next

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2

        # if not curr2:
        #     return curr1
        # if not curr1:
        #     return curr2
        #
        # if curr1.val <= curr2.val:
        #     hVal = curr1.val
        #     curr1 = curr1.next
        # else:
        #     hVal = curr2.val
        #     curr2 = curr2.next

        head = ListNode()
        prev = head

        while curr1 or curr2:
            if not curr2:
                nVal = curr1.val
                curr1 = curr1.next

            elif not curr1:
                nVal = curr2.val
                curr2 = curr2.next

            elif curr1.val <= curr2.val:
                nVal = curr1.val
                curr1 = curr1.next
            else:
                nVal = curr2.val
                curr2 = curr2.next

            n = ListNode(nVal)
            prev.next = n
            prev = n

        return head.next


if __name__ == "__main__":
    s = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    # list1 = None
    # list2 = None

    print(s.duplicateList(list1))

    # print(s.mergeTwoLists(list1, list2))
