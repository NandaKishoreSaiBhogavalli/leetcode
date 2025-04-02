class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
        for num in num_set:
            is_start_sequence = (num-1 not in num_set)
            if is_start_sequence:
                current_streak = 1
                next_num = num+1
                while next_num in num_set:
                    current_streak += 1
                    next_num +=1
                longest = max(longest,current_streak)
        return longest
