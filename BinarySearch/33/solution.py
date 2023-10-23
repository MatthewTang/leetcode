class Solution:
    def search(self, nums: list[int], t: int) -> int:
        # sol 1, pointer approach
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == t:
                return l
            if nums[r] == t:
                return r

            if nums[l] < nums[r]:
                if t < nums[l] or t > nums[r]:
                    return -1
                else:
                    m = (l + r) // 2
                    if nums[m] == t:
                        return m

                    if nums[m] > t:
                        r = m - 1
                    else:
                        l = m + 1
            else:
                m = (l + r) // 2
                if nums[m] == t:
                    return m

                if nums[l] < nums[m]:
                    if nums[m] >= t >= nums[l]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    if nums[r] >= t >= nums[m]:
                        l = m + 1
                    else:
                        r = m - 1
        return -1
        # time complexity: O(n)


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(s.search([1], 0))
    print(s.search([1, 2, 3, 4, 5], 2))
