class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        total_without_duplicates = sum(set(nums))
        duplicate_element = total - total_without_duplicates
        n = len(set(nums)) + 1
        sum_of_n_nums = n * (n + 1) / 2
        missing_element = total_without_duplicates - sum_of_n_nums
        return [duplicate_element, abs(missing_element)]
