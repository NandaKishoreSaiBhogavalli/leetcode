class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(map(str, digits))) + 1
        return list(map(int, str(num)))

        # This is an easy approach which can be much understandable
        # num = "".join(map(str,digits))
        # plus_one = int(num)+1
        # arr = []
        # while plus_one > 0:
        #     rem = plus_one%10
        #     arr.append(rem)
        #     plus_one//=10
        # return arr[-1::-1]




