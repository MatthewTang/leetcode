class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # # sol 1, works
        # countT = {}
        #
        # for i in range(len(t)): # O(n), given n == t.length
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        #
        # res = ""
        # countS = {}
        # l = 0
        # for r in range(len(s)): # O(m)
        #     countS[s[r]] = 1 + countS.get(s[r], 0)
        #
        #     valid = True
        #     for _, i in enumerate(countT.items()): # O(26)
        #         if countS.get(i[0], 0) < i[1]:
        #             valid = False
        #             break
        #     if not valid:
        #         continue
        #
        #     if len(res) == 0 or r - l + 1 < len(res):
        #         res = s[l : r + 1]
        #
        #     while countS[s[l]] - 1 >= countT.get(s[l], 0):
        #         countS[s[l]] -= 1
        #         l += 1
        #         if r - l + 1 < len(res):
        #             res = s[l : r + 1]
        #
        # return res
        # # time complexity: ~ O(n) + O(26m) = ~O(m)

        # sol 2
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update res
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        
        # time complexity: O(n)


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow("a", "a"))
    print(s.minWindow("a", "aa"))
    print(s.minWindow("aa", "aa"))
