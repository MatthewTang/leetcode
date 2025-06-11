import unittest
from typing import List, Optional


class Node:
    def __init__(self, val=None, next=None, random=None) -> None:
        self.val = val
        self.next = next
        self.random = random
        self._id = id(self)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return False
        return self._id == other._id

    def __hash__(self) -> int:
        return self._id

    def equal(self, other, visited=None):
        if not visited:
            visited = set()

        pair = (self._id, other._id)
        if pair in visited:
            return True
        visited.add(pair)

        if not isinstance(other, Node):
            return False

        if self.val != other.val:
            return False

        if self.next or other.next:
            if not self.next or not other.next:
                return False
            if not self.next.equal(other.next, visited):
                return False

        if self.random or other.random:
            if not self.random or not other.random:
                return False
            if not self.random.equal(other.random, visited):
                return False

        return True


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        original_to_copy = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            original_to_copy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = original_to_copy[curr]
            copy.next = original_to_copy[curr.next] if curr.next else curr.next
            copy.random = original_to_copy[curr.random] if curr.random else curr.random
            curr = curr.next

        return original_to_copy[head] if head else head

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            copy = curr.next
            copy.random = curr.random.next if curr.random else None
            curr = copy.next
        curr = head
        head = curr.next if curr else None
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next

        return head


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        node0 = Node(7)
        node1 = Node(13)
        node2 = Node(11)
        node3 = Node(10)
        node4 = Node(1)

        node0.next = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

        node1.random = node0
        node2.random = node4
        node3.random = node2
        node4.random = node0

        result = s.copyRandomList(node0)
        self.assertTrue(result.equal(node0))

    def test2(self):
        s = Solution()
        result = s.copyRandomList(None)
        self.assertIsNone(result)

    def test3(self):
        s = Solution()
        node0 = Node(1)
        node1 = Node(2)
        node0.next = node1
        node0.random = node1
        node1.random = node1
        result = s.copyRandomList(node0)
        self.assertTrue(result.equal(node0))

    def test3(self):
        s = Solution()
        node0 = Node(3)
        node1 = Node(3)
        node2 = Node(3)
        node0.next = node1
        node1.next = node2
        node1.random = node0
        result = s.copyRandomList(node0)
        self.assertTrue(result.equal(node0))


if __name__ == "__main__":
    unittest.main()
