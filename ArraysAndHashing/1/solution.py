class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]

        """

        # sol 1 O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #
        # return [];

        # sol 2 O(n)
        val_idx_map = {}  # val -> idx

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in val_idx_map:
                return [val_idx_map[diff], idx]
            val_idx_map[num] = idx


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
