from typing import Optional, List


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

    # solution 1
    # time complexity: O(nk)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy

        while not all(i is None for i in lists):

            min_val = float("inf")
            index = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:
                    index = i
                    min_val = lists[i].val
            head.next = ListNode(min_val)
            head = head.next
            lists[index] = lists[index].next

        return dummy.next

    # solution 2
    # time complexity: O(nlogk)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.mergeLists(l1, l2))
            lists = merged_lists

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode(0)
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next

            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    l0 = head = ListNode()
    l1 = ListNode(1, ListNode(2))
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l3 = ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))
    )

    # print(s.mergeKLists([l0]))
    print(s.mergeKLists([l1, l2, l3]))
