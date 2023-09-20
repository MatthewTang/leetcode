class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # sol 1 (brute force)
        # nums = [1,2,3,4]

        # init n size array
        # [1, 1, 1, 1]

        # first iteration
        # [1, 1, 1, 1]

        # second iteration
        # [2, 1, 2, 2]

        # third iteration
        # [6, 3, 2, 6]

        # nth iteration
        # [24, 12, 8, 6]

        # products = [1 for _ in nums]  # array with len n
        #
        # for i in range(len(nums)):  # O(n)
        #     for j in range(len(products)):  # O(n)
        #         if i == j:
        #             continue
        #         products[j] *= nums[i]
        #
        # return products

        # time complexity: O(n^2)

        # sol 2 (prefix, postfix array)
        # nums = [1, 2, 3, 4]
        # prefix = [1, 2, 6, 24]
        # postfix = [24, 24, 12, 4]
        # out = [24, 12, 8, 6]

        # prefixes = [1 for _ in nums]  # O(n)
        # for i in range(len(nums)):  # O(n)
        #     num = nums[i]  # O(1)
        #     if i == 0:
        #         prefixes[i] = 1 * num  # O(1)
        #     else:
        #         prefixes[i] = prefixes[i - 1] * num  # O(1)
        #
        # postfixes = [1 for _ in nums]  # O(n)
        # for i in range(len(nums) - 1, -1, -1):  # O(n)
        #     num = nums[i]
        #
        #     if i == len(nums) - 1:
        #         postfixes[i] = 1 * num
        #     else:
        #         postfixes[i] = postfixes[i + 1] * num
        #
        # out = []
        # for i in range(len(nums)):  # O(n)
        #     if i == 0:
        #         prefix = 1  # O(1)
        #     else:
        #         prefix = prefixes[i - 1]  # O(1)
        #
        #     if i == len(nums) - 1:
        #         postfix = 1  # O(1)
        #     else:
        #         postfix = postfixes[i + 1]  # O(1)
        #
        #     out.append(prefix * postfix)  # O(1)
        #
        # return out

        # O(n) + O(n) + O(n) + O(n) + O(n) -> O(5n) -> O(n)

        # sol 3 (pre, pos with O(1) mem)
        # nums = [1, 2, 3, 4]
        # prev = 1 * 1 * 2 * 3

        # [1, 1, 2, 6]
        # post = 1 * 4  * 3 * 2
        # [ 24, 12  ,8 ,6]

        out = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            out[i] = prev
            prev *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= post
            post *= nums[i]

        return out


if __name__ == "__main__":
    s = Solution()

    tests = [[1, 2, 3, 4], [-1, 1, 0, -3, 3]]

    for test in tests:
        print(s.productExceptSelf(test))

    # print(s.productExceptSelf(tests[0]))
