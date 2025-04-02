# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_sum = nums[0]
#         current_sum = nums[0]
#         for num in range(1,len(nums)):
#             current_sum = max(nums[num],current_sum+nums[num])
#             max_sum = max(max_sum,current_sum)
#         return max_sum


def maxSubArray( nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        uniques = list(set(nums))
        unique = []
        for i in uniques:
            if i<0:
                continue
            else:
                unique.append(i)
        max_sum = unique[0]
        current_sum = unique[0]
        for num in range(1,len(unique)):

            current_sum = max(unique[num],current_sum+unique[num])
            max_sum = max(max_sum,current_sum)
        return max_sum

nums = [-2,2,7]
print(maxSubArray(nums))

