class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []

        for i in s:
            if i in brackets.values():  # O(3)
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                c = stack.pop()  # O(1)
                if c != brackets.get(i, 0):  # O(1)
                    return False

        return len(stack) == 0

        # time complexity: O(3n) ~ O(n), given s.length = n
        # space complexity: O(n)


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("["))
    print(s.isValid("]"))
