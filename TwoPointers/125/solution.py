class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # sol 1 using two pointers
        # Remove all non-alphanumeric characters
        # s = ''.join([c.lower() for c in s if c.isalnum()]) # O(n)

        # for i in range(len(s)//2): # O(n)
        #     if s[i] != s[len(s)-1-i]:
        #         return False
        #
        # return True

        # time complexity: O(n), O(1)

        # sol 2
        # Remove all non-alphanumeric characters
        # s = ''.join([c.lower() for c in s if c.isalnum()]) # O(n)

        # reverse the word, then compare equality
        # rs = s[::-1] # O(n)

        # return s == rs

        # time complexity also O(n) and memory O(n), memory O(n)

        # sol 3
        l, r = 0, len(s) - 1

        while l < r:
            if not self.alphaNumeric(s[l]):
                l += 1
                continue
            if not self.alphaNumeric(s[r]):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

        # time complexity: O(n), memory complexity: O(1)

    def alphaNumeric(self, c):
        return (
            ord("a") <= ord(c) <= ord("z")
            or ord("A") <= ord(c) <= ord("Z")
            or ord("0") <= ord(c) <= ord("9")
        )


if __name__ == "__main__":
    s = Solution()
    tests = ["A man, a plan, a canal: Panama", "race a car", " "]
    for test in tests:
        print(s.isPalindrome(test))
