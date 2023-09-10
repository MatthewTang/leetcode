from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) != len(t):
        #     return False
        #
        # s_map = {}
        #
        # # sol 1
        # for i in range(len(s)):
        #     char = s[i]
        #     count = s_map.get(char)
        #     s_map[char] = count + 1 if count else 1
        #
        # t_map = {}
        #
        # for i in range(len(t)):
        #     char = t[i]
        #
        #     s_count = s_map.get(char)
        #     if not s_count:
        #         return False
        #
        #     t_count = t_map.get(char)
        #     t_map[char] = t_count + 1 if t_count else 1
        #
        # for char, count in s_map.items():
        #     t_count = t_map.get(char)
        #     if not t_count or t_count != count:
        #         return False
        #
        # return True

        # sol 2 (only loop once)
        # if len(s) != len(t):
        #     return False
        #
        # countS, countT = {}, {}
        #
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT

        # sol 3 (just one dict)
        # won't get key error if count[k] if doesn't exist, return 0 for int instead
        # counts = defaultdict(int)
        #
        # for char in s:
        #     counts[char] += 1
        #
        # for char in t:
        #     counts[char] -= 1
        #
        # for c in counts.values():
        #     if c != 0:
        #         return False
        #
        # return True

        # sol 4 (similar to sol3, but uses array)
        zero = ord("a")
        counts = [0] * 25

        for char in s:
            char_idx = ord(char) - zero
            counts[char_idx] += 1

        for char in t:
            char_idx = ord(char) - zero
            counts[char_idx] -= 1

        for count in counts:
            if count != 0:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))
