class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniques = set(nums)

        filtered = [num for num in uniques if num >= 0]  # Keep only non-negative numbers

        #Handle the case where all numbers are negative
        if not filtered:
            return max(nums)  # Return the maximum number from the original list

        #  Initialize max_sum and current_sum
        max_sum = filtered[0]
        current_sum = filtered[0]

        # Apply Kadane's algorithm
        for num in filtered[1:]:
            current_sum = max(num, current_sum + num)  # Update current_sum
            max_sum = max(max_sum, current_sum)  # Update max_sum

        return max_sum
