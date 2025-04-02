class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if n<k:
            return None

        window_sum = sum(nums[:k])
        max_sum = window_sum
        left = 0
        for i in range(k,n):
            window_sum+=nums[i]
            window_sum-=nums[left]
            left+=1
            max_sum = max(max_sum,window_sum)
        return float(max_sum)/k


