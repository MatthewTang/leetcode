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
    # # iterative #1
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     vArray = []
    #     curr = head
    #     while curr:
    #         vArray.append(curr.val)
    #         curr = curr.next
    #
    #     nN = None
    #     for v in vArray:
    #         nN = ListNode(v, nN)
    #
    #     # while vArray:
    #     #     nN = ListNode(vArray.pop(), nN)
    #
    #     return nN

    # # iterative  # 2 (simplified w/o the creation of list)
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #
    #     curr = head
    #     nN = None
    #     while curr:
    #         nN = ListNode(curr.val, nN)
    #         curr = curr.next
    #
    #     return nN

    # iterative # 3 neetcode, no need create new nodes
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        # time complexity: O(n), space complexity: O(1)

    # # recursive approach #1
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head: return head
    #
    #     def fn(curr: Optional[ListNode], next: Optional[ListNode]):
    #         nN = ListNode(curr.val, next)
    #
    #         if not curr.next:
    #             return nN
    #         else:
    #             return fn(curr.next, nN)
    #
    #     return fn(head, None)

    # # recursive approach #2
    # # tc: O(n), sc: O(n)
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     def fn(curr: Optional[ListNode], prev: Optional[ListNode]):
    #         if not curr:
    #             return prev
    #         else:
    #             return fn(curr.next, ListNode(curr.val, prev))
    #
    #     return fn(head, None)

    # recursive approach #3, w/o create new nodes
    # tc: O(n), sc: O(n)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def fn(curr: Optional[ListNode], prevs: list[ListNode]):
            if not curr:
                return None
            else:
                prev = fn(curr.next, prevs)
                curr.next = None
                if prev:
                    prevs.append(prev)
                    prev.next = curr

                return curr

        prevs = []
        prev = fn(head, prevs)
        prevs.append(prev)
        return prevs[0]
        # return prevs[0] if len(prevs) > 0 else None

    # # duplicate the list by recursion
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
    head = None
    print(s.reverseList(head))

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(head)
    print(s.reverseList(head))

    head = ListNode(1, ListNode(2))
    print(head)
    print(s.reverseList(head))

    head = ListNode()
    print(head)
    print(s.reverseList(head))

    # assert s.reverseList(head) == ListNode(
    #     5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))
    # )

    # assert s.reverseList(head) == head
