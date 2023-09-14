from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs: list[str]):
        return

    def groupAnagrams(self, strs: list[str]):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_str_unsorted_strs_map = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))

            # tried this but doesn't work bc list.append doesn't return the list
            # sorted_unsorted_map[sorted_str] = sorted_unsorted_map[sorted_str].append(
            #     str
            # )
            # shd instead be
            sorted_str_unsorted_strs_map[sorted_str].append(str)

        out = []

        for unsorted_strs in sorted_str_unsorted_strs_map.values():
            out.append(unsorted_strs)

        return out


if __name__ == "__main__":
    s = Solution("matt")
    tests = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]
    for test in tests:
        print(s.groupAnagrams(test))
