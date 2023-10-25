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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.reverseList(head))

    # assert s.reverseList(head) == ListNode(
    #     5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
    # )

    assert s.reverseList(head) == head
