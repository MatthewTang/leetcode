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
            if node.val in result:
                result.append(node.val)
                break

            result.append(node.val)
            node = node.next
        return result

    def __repr__(self) -> str:
        return str(self.to_list())


class Solution:

    # hash map solution
    # time: O(n), space: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while head:
            if head in visited:
                return True

            visited.add(head)
            head = head.next

        return False

    # # two pointers solution
    # # time: O(n), space: O(1)
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     slow, fast = head, head
    #
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #         if slow == fast:
    #             return True
    #
    #     return False


if __name__ == "__main__":
    s = Solution()
    # no cycle
    head = ListNode(1)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # # has cycle
    head = ListNode(1)
    head.next = head

    # # has cycle on 2
    # head = ListNode(1, ListNode(2))
    # head.next.next = head

    # # has cycle on 4 (last) back to 2
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    # head.next.next.next.next = head.next

    print(s.hasCycle(head))
