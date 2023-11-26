from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


def printTree(root: TreeNode, level=0):
    if root is None:
        return
    printTree(root.right, level + 1)
    print("\t" * level, root.val)
    printTree(root.left, level + 1)


class Solution:
    # # recursive dfs
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     def compare(p: Optional[TreeNode], q: Optional[TreeNode]):
    #         if not p and not q:
    #             return True
    #
    #         if not p or not q:
    #             return False
    #
    #         if p.val != q.val:
    #             return False
    #
    #         return compare(p.left, q.left) and compare(p.right, q.right)
    #
    #     return compare(p, q)

    # # iterative dfs
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     pstack, qstack = [p], [q]
    #
    #     while pstack or qstack:
    #         if not pstack or not qstack:
    #             return False
    #
    #         pn = pstack.pop()
    #         qn = qstack.pop()
    #
    #         if not pn and not qn:
    #             continue
    #
    #         if not pn or not qn:
    #             return False
    #
    #         if qn.val != pn.val:
    #             return False
    #
    #         pstack.append(pn.left)
    #         pstack.append(pn.right)
    #
    #         qstack.append(qn.left)
    #         qstack.append(qn.right)
    #
    #     return True

    # bfs
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq, qq = deque(), deque()
        pq.append(p)
        qq.append(q)

        while pq or qq:
            if not pq or not qq:
                return False
            pn, qn = pq.popleft(), qq.popleft()

            if not pn and not qn:
                continue

            if not pn or not qn:
                return False

            if pn.val != qn.val:
                return False

            pq.append(pn.left)
            pq.append(pn.right)
            qq.append(qn.left)
            qq.append(qn.right)

        return True


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(17)

    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(17)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    root3 = TreeNode()
    root4 = None

    # printTree(root)
    print(solution.isSameTree(root1, root))
    print(solution.isSameTree(root4, root3))
