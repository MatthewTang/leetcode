class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Sol 1 O(n)
        # val_idx_map = {}
        #
        # for idx, num in enumerate(numbers):
        #     diff = target - num
        #     if diff in val_idx_map:
        #         return [val_idx_map[diff] + 1, idx + 1]
        #     val_idx_map[num] = idx
        #
        # return []

        # Sol 2: two pointers
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]

            if s > target:
                r -= 1
                continue

            # s < target
            l += 1

        return []

        # time complexity: O(n), bc we only traverse the list once


if __name__ == "__main__":
    s = Solution()
    tests = [
        {"numbers": [2, 7, 11, 15], "target": 9},
        {"numbers": [2, 3, 4], "target": 6},
        {"numbers": [-1, 0], "target": -1},
    ]
    for test in tests:
        print(s.twoSum(test["numbers"], test["target"]))
