class Solution:
    def findMin(self, nums: list[int]) -> int:

        # # sol 1
        # return min(nums) # O(n)

        # sol 2, recursively splitting nums in half and finding minimum, #O(log n)
        return self._fn(nums)

    def _fn(self, nums: list[int]):
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        m = len(nums) // 2
        l = nums[0:m]
        r = nums[m : len(nums)]

        return min(self._fn(l), self._fn(r))


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(s.findMin([11, 13, 15, 17]))
