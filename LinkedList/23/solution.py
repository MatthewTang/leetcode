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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists[0] = lists[0].next
        # for i in range(len(lists)):
        #     print(lists[i].val)
        return all(i is None for i in lists)


if __name__ == "__main__":
    s = Solution()
    l0 = head = ListNode(1)
    l1 = ListNode(1, ListNode(2))
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # head = ListNode(
    #     1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))
    # )

    # print(s.mergeKLists([l1, l2]))
    print(s.mergeKLists([l0]))
