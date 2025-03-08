class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)+1
        expected_sum = n*(n-1)/2
        sum_of_nums = sum(nums)
        missing_num = expected_sum - sum_of_nums
        return missing_num
s = Solution()
print(s.missingNumber([0,1,2,4]))