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

    # # first try, doesn't work, since new Node is returned
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     # create array
    #     arr = []
    #     curr = head
    #     while curr:
    #         arr.append(curr.val)
    #         curr = curr.next
    #
    #     isOdd = len(arr) % 2
    #     mid = len(arr) // 2
    #
    #     dummy = ListNode()
    #     tail = dummy
    #
    #     for i in range(mid):
    #         n = ListNode(arr[i])
    #         tail.next = n
    #         tail = n
    #
    #         n = ListNode(arr[len(arr) - i - 1])
    #         tail.next = n
    #         tail = n
    #
    #     if isOdd:
    #         n = ListNode(arr[mid])
    #         tail.next = n
    #         tail = n
    #
    #     return dummy.next

    # # time complexity: O(n), space complexity: O(n)
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     # create array
    #     arr = []
    #     curr = head
    #     while curr:
    #         arr.append(curr)
    #         curr = curr.next
    #
    #     mid = len(arr) // 2
    #
    #     for i in range(mid):
    #         n = arr[i]
    #         n.next = arr[len(arr) - i - 1]
    #
    #         n = n.next
    #         n.next = arr[i + 1]
    #
    #     n = arr[mid]
    #     n.next = None
    #
    #     return arr[0]

    # time complexity: O(n), space complexity: O(1) neetcode's solution
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        second = s.next
        prev = s.next = None  # set mid.next to none
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head


if __name__ == "__main__":
    s = Solution()
    # head = ListNode(
    #     1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))
    # )
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    head = ListNode()
    print(s.reorderList(head))
