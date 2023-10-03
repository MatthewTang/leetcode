class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # sol 1: brute force
        # areas = []
        m = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                l = j - i
                h = min(height[i], height[j])
                # areas.append(l * h)
                area = l * h
                if area > m:
                    m = area

        # return max(areas)
        return m

        # time complexity: O(n^2) + O(n) = O(n^2), note can use max heap for areas but still O(n^2)
        # space complexity: O(n)/ O(1)

        # # sol 2: 2 pointers
        # l = 0
        # r = len(height) - 1
        #
        # m = 0
        # while l < r:
        #     length = r - l
        #     h = min(height[l], height[r])
        #     area = length * h
        #     if area > m:
        #         m = area
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        #
        # return m
        # 
        # # time complexity: O(n)
        # # space complexity: O(1)



if __name__ == "__main__":
    s = Solution()
    tests = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1]]

    for test in tests:
        print(s.maxArea(test))
