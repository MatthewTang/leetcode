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
    # sol 1
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     p2 = head
    #     c = 0
    #     while c < n:
    #         c += 1
    #         p2 = p2.next
    #     p1, p0 = head, None
    #
    #     while p2:
    #         p0 = p1
    #         p2 = p2.next
    #         p1 = p1.next
    #
    #     if p0:
    #         p0.next = p1.next
    #     else:
    #         head = p1.next
    #     return head

    # sol 2 use dummy
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            n -= 1
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    # head = ListNode(
    #     1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))
    # )
    # n = 2

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n = 2

    # head = ListNode(1)
    # n = 1

    # head = ListNode(1, ListNode(2))
    # n = 2

    print(s.removeNthFromEnd(head, n))
