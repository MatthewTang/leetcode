from collections import defaultdict
import heapq


class Solution(object):
    def topKFrequent(self, nums, k) -> list[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # print(nums)

        # sol 1 (hashmap, sort array/lists)
        # num_freq_map = defaultdict(int)  # num -> freq
        #
        # for num in nums: # O(n)
        #     num_freq_map[num] += 1
        #
        # # print(num_freq_map)
        #
        # k_freq = [0] * k
        # k_num = [0] * k
        #
        # for num in num_freq_map.keys(): # O(n)
        #     freq = num_freq_map[num]
        #     if freq > k_freq[0]:
        #         k_freq[0] = freq
        #         k_num[0] = num
        #
        #         for i in range(k - 1): # O(n) bc max k = n
        #             if k_freq[i] <= k_freq[i + 1]:
        #                 break
        #
        #             tmp = k_freq[i]
        #             k_freq[i] = k_freq[i + 1]
        #             k_freq[i + 1] = tmp
        #
        #             tmp = k_num[i]
        #             k_num[i] = k_num[i + 1]
        #             k_num[i + 1] = tmp
        #
        # return k_num

        # time complexity: O(n) + O(n^2) -> O(n^2)

        # sol 2 (hashmap, max heap)
        # freq = {}
        # for num in nums:  # O(n)
        #     freq[num] = freq.get(num, 0) + 1
        #
        # heap = []
        # for num, count in freq.items():  # O(n)
        #     if len(heap) < k:
        #         heapq.heappush(heap, (count, num))  # O(log n)
        #     elif count > heap[0][0]:
        #         heapq.heappop(heap)  # O(log n)
        #         heapq.heappush(heap, (count, num))  # O(log n)
        #
        # return [num for _, num in heap]

        # time complexity: O(n) + O(n log n) -> O(n log(n))

        # sol 3 (bucket sort)
        # 3.1
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1
        #
        # bucket = [[] for _ in nums]
        #
        # for val, count in freq.items():
        #     bucket[count - 1].append(val)
        #
        # out = []
        # for i in range(len(nums) - 1, -1, -1):
        #     for j in bucket[i]:
        #         out.append(j)
        #         if len(out) == k:
        #             return out

        # 3.2
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n, c in count.items():
            freq[c].append(n)

        out = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                out.append(n)
                if len(out) == k:
                    return out


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))
