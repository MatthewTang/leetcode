# O(n^3)
# get every triplet of elements in the array
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            print(nums[i], nums[j], nums[k])


# get every pair of elements in the array
# nums = [1, 2, 3]
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         print(nums[i], nums[j])

# print([i for i in range(4,3)])
