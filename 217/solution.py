class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # sol 1/2
        m = {}
        for i in range(len(nums)):
            num = nums[i]
            count = m.get(num)
            m[num] = count + 1 if count else 1

            # if count: return True
            # m[num] = 1

        for i in m.values():
            if i > 1:
                return True

        return False

        # sol 3
        # s = set(nums)
        # return not len(s) == len(nums)

        # sol 4
        # for i in range(len(nums)):
        #     for j in range(len(nums) - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             tmp = nums[j]
        #             nums[j] = nums[j + 1]
        #             nums[j + 1] = tmp
        #
        # # print(nums)
        #
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        #
        # return False


if __name__ == "__main__":
    s = Solution()
    tests = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

    for nums in tests:
        print(s.containsDuplicate(nums))
