class Solution:
    def search(self, nums: list[int], t: int) -> int:
        # # sol 1, pointer approach
        # l = 0
        # r = len(nums) - 1
        #
        # while l <= r:
        #     if nums[l] == t:
        #         return l
        #     if nums[r] == t:
        #         return r
        #
        #     if nums[l] < nums[r]:
        #         if t < nums[l] or t > nums[r]:
        #             return -1
        #         else:
        #             m = (l + r) // 2
        #             if nums[m] == t:
        #                 return m
        #
        #             if nums[m] > t:
        #                 r = m - 1
        #             else:
        #                 l = m + 1
        #     else:
        #         m = (l + r) // 2
        #         if nums[m] == t:
        #             return m
        #
        #         if nums[l] < nums[m]:
        #             if nums[m] >= t >= nums[l]:
        #                 r = m - 1
        #             else:
        #                 l = m + 1
        #         else:
        #             if nums[r] >= t >= nums[m]:
        #                 l = m + 1
        #             else:
        #                 r = m - 1
        # return -1
        # # time complexity: O(n)

        # sol 2, recursive
        return self._bs(nums, t, 0)

    def _bs(self, nums, t, idx):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return idx if nums[0] == t else -1

        m = len(nums) // 2

        if nums[m] == t:
            return idx + m

        if nums[0] < nums[-1]:
            if nums[m] > t:
                return self._bs(nums[:m], t, idx)
            else:
                return self._bs(nums[m + 1 :], t, idx + m + 1)
        else:
            if nums[0] < nums[m]:
                if nums[m] >= t >= nums[0]:
                    return self._bs(nums[:m], t, idx)
                else:
                    return self._bs(nums[m + 1 :], t, idx + m + 1)
            else:
                if nums[m] <= t <= nums[-1]:
                    return self._bs(nums[m + 1 :], t, idx+m+1)
                else:
                    return self._bs(nums[:m], t, idx)


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 1))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 6))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 4))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 5))
    print(s.search([1], 0))
    print(s.search([], 0))
    print(s.search([1, 2, 3, 4, 5], 2))
