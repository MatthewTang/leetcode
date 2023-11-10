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
    def duplicateList(self, list):
        # curr = list
        # head = None
        # prev = None
        # while curr:
        #     if not head:
        #         head = ListNode(curr.val)
        #         prev = head
        #         curr = curr.next
        #         continue
        #
        #     n = ListNode(curr.val)
        #     prev.next = n
        #     prev = n
        #     curr = curr.next
        #
        # return head

        curr = list
        head = ListNode(curr.val)
        prev = head
        curr = curr.next

        while curr:
            n = ListNode(curr.val)
            prev.next = n
            prev = n
            curr = curr.next

        return head

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        return list1, list2


if __name__ == "__main__":
    s = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    # print(s.mergeTwoLists(list1, list2))
    print(s.duplicateList(list1))
