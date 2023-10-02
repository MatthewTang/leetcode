# sol1 brute force
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         cs = []
#         for i in range(len(nums)): # O(n^3)
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     cs.append([nums[i], nums[j], nums[k]])
#
#         scs = [sorted(c) for c in cs if sum(c) == 0] # O(n^3)
#
#         out = []
#
#         for c in scs: # O(N^3)
#             if c not in out:
#                 out.append(c)
#
#         return out
#         # time complexity O(n^3)

# sol 2 for each num, find two sum using hash table
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         sorted_nums = sorted(nums)
#
#         s = set([])
#         out = []
#
#         for i in range(len(sorted_nums)):
#             n = sorted_nums[i]
#             if n in s:
#                 continue
#             s.add(n)
#             ns = sorted_nums[i + 1 :]
#             out = self.twoSum(ns, n, out)
#
#         return out
#
#     def twoSum(self, nums, num, out):
#         target = 0 - num
#         s = set([])
#         added = set([])
#
#         for _num in nums:  # O(n)
#             diff = target - _num
#             # if diff in s and [num, diff, _num] not in out:
#             if diff in s and _num not in added:
#                 added.add(_num)
#                 out.append([num, diff, _num])
#             s.add(_num)
#
#         return out
#
#     # time complexity(?) O(n^3), bc twoSum is O(n^2) bc for each num in nums, we change if num in out and out is size n in worst case
#
#     # time complexity O(n^2) bc twoSum is O(n), set lookup is O(1)


# sol 3 for each num, find two sum using two pointers
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sorted_nums = sorted(nums)  # O(nlogn)
        s = set([])
        out = []

        for i in range(len(sorted_nums)):  # O(n)
            n = sorted_nums[i]
            if n in s:
                continue
            s.add(n)
            ns = sorted_nums[i + 1 :]
            out = self.twoSum(ns, n, out)  # O(n)

        return out

    def twoSum(self, nums, num, out):
        target = 0 - num
        l = 0
        r = len(nums) - 1
        s = set([])

        while l < r:  # O(n)
            if nums[l] in s:
                l += 1
                continue

            _sum = nums[l] + nums[r]

            if _sum == target:
                s.add(nums[l])
                out.append([num, nums[l], nums[r]])
                l += 1
                r -= 1
                continue

            if _sum < target:
                l += 1
                continue

            if _sum > target:
                r -= 1
                continue

        return out

    # time complexity O(nlogn + n^2) = O(n^2)
    # space complexity O(n) bc we use set to store unique nums


if __name__ == "__main__":
    s = Solution()
    tests = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0, 0],
        [-2, 0, 0, 2, 2],
        [3, 0, -2, -1, 1, 2],
    ]

    for test in tests:
        print(s.threeSum(test))

    # print(s.threeSum(tests[5]))
