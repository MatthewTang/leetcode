class Solution:
    def findMin(self, nums: list[int]) -> int:

        # # sol 1
        # return min(nums) # O(n)

        # # sol 2, recursively splitting nums in half and finding minimum, #O(log n)
        # if len(nums) == 1 or nums[0] < nums[-1]:
        #     return nums[0]
        #
        # m = len(nums) // 2
        # l = nums[0:m]
        # r = nums[m : len(nums)]
        #
        # return min(self.findMin(l), self.findMin(r))

        # sol 3, iterative, #O(log n), pointer approach
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(s.findMin([11, 13, 15, 17]))
