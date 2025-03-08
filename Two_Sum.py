class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i,num in enumerate(nums):
            number = target-num
            if number in dictionary:
                return [dictionary[number],i]
            dictionary[num] = i
        return None