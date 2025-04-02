# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dictionary = {}
#         for i,num in enumerate(nums):
#             number = target-num
#             if number in dictionary:
#                 return [dictionary[number],i]
#             dictionary[num] = i
#         return None

def findMaxAverage( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    n = len(nums)
    if n < k:
        return None  # Edge case: If the array is too small

    window_sum = sum(nums[:k]) # Compute initial sum
    max_sum = window_sum  # Track max sum
    left = 0

    for i in range(k, n):
        window_sum += nums[i]  # Add new element
        window_sum -= nums[left]  # Remove old element
        left += 1
        max_sum = max(max_sum, window_sum)  # Ensure max_sum updates correctly

    return float(max_sum) / k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))