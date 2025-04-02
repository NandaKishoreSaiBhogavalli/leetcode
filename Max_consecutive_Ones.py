from idlelib.sidebar import ShellSidebar


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcount=0
        currentcount=0
        for digit in nums:
            if digit==1:
                currentcount+=1
            else:
                currentcount=0
            maxcount = max(currentcount,maxcount)
        return maxcount



arr = [1,4,3,2]
arr.sort()
currmin=0
total=0
for digit in range(0,len(arr)-1,2):
    currmin=min(arr[digit], arr[digit+1])
    total+=currmin
print(total)



