class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        unique = set(arr)
        for i in arr:
            if i==0:
                if arr.count(0)>1:
                    return True
            elif (2*i) in unique:
                return True
        return False



