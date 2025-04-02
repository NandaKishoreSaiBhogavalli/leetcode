class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        currentmin=0
        total=0
        for digit in range(0,len(nums)-1,2):
            currentmin=min(nums[digit],nums[digit+1])
            total+=currentmin
        return total