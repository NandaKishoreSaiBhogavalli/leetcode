# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         s1 = set(nums1)
#         s2 = set(nums2)
#         common = list(s1.intersection(s2))
#         return common

def findMaxAverage( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    n = len(nums)
    if n < k:
        return None

    window_sum = sum(nums[:k])
    max_sum = window_sum
    left = 0
    for i in range(k, n):
        window_sum += nums[i]
        window_sum -= nums[left]
        left += 1
        max_sum = (max_sum, window_sum)
    return float(max_sum) / k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))