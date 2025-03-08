class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1,-1
        try:
            first = nums.index(target)
        except Exception:
            return -1,-1
        last = first
        for i in range(first+1,len(nums)):
            if nums[i]==target:
                last = i
        return first,last