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
        # # iterative
        # vArray = []
        # curr = head
        # while curr:
        #     vArray.append(curr.val)
        #     curr = curr.next
        #
        #
        # nN = None
        # for v in vArray:
        #     nN = ListNode(v, nN)
        #
        # # while vArray:
        # #     nN = ListNode(vArray.pop(), nN)
        #
        # return nN

        # recursive approach
        def fn(curr: Optional[ListNode], next: Optional[ListNode]):
            nN = ListNode(curr.val, next)

            if not curr.next:
                return nN
            else:
                return fn(curr.next, nN)

        return fn(head, None)

        # def fn(curr: Optional[ListNode]):
        #
        #     if not curr.next:
        #         return ListNode(curr.val)
        #
        #     return ListNode(curr.val, fn(curr.next))
        #
        # return fn(head)


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.reverseList(head))

    # assert s.reverseList(head) == ListNode(
    #     5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
    # )

    # assert s.reverseList(head) == head
