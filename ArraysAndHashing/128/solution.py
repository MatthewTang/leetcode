import heapq


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sol 1 sort list
        # nums = sorted(nums)  # O(n log(n))
        #
        # curr = nums[0]
        # k = 1
        # t = 1
        # for i in range(1, len(nums)): # O(n)
        #     if nums[i] == curr + 1:
        #         t += 1
        #         curr += 1
        #     else:
        #         t = 1
        #         curr = nums[i]
        #     if t > k:
        #         k = t
        #
        # return k

        # O(nlog(n)) + O(n) -> O(n log(n))
        ##############################################

        # sol 2 add list to heap
        # heapq.heapify(nums)  # O(n)
        #
        # while len(nums):  # O(n)
        #     nextMin = heapq.heappop(nums)  # O(log(n))

        # similar to sol 1, still O(n log(n))

        ##############################################
        # sol 3
        # hashmap to get count
        # count = {}
        # for i in range(len(nums)):  # O(n)
        #     num = nums[i]
        #     count[num] = i
        #
        # prevs = [-1] * len(nums)  # O(0)
        # for i in range(len(nums)):  # O(n)
        #     num = nums[i]
        #     if num - 1 in count:
        #         prevs[i] = count[num - 1]
        #
        # k = 0
        # for i in range(len(prevs)):  # O(n^2)
        #     if prevs[i] < 0:
        #         l = 1
        #     else:
        #         l = self.find(i, prevs) + 1
        #
        #     if l > k:
        #         k = l
        #
        # return k
        ##############################################

        # sol 4
        numSet = set(nums)  # O(n)
        longest = 0

        for num in nums: # O(n)
            if num - 1 not in numSet:

                # tmp = 1
                # next = num + 1
                # while next in nums:
                #     tmp += 1
                #     next += 1
                # if tmp > longest:
                #     longest = tmp

                ## alternative
                length = 0
                while num + length in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

    # for sol 3
    # def find(self, i, prevs):
    #     j = prevs[i]
    #     l = 1
    #     while prevs[j] > -1:
    #         tmp = prevs[j]
    #         j = tmp
    #         l += 1
    #     return l


if __name__ == "__main__":
    s = Solution()
    tests = [[100, 4, 200, 1, 3, 2], [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], [], [0]]

    for test in tests:
        print(s.longestConsecutive(test))

    # print(s.longestConsecutive(tests[1]))
