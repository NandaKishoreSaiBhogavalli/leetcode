class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        Original = x
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            rem = x % 10
            rev = (rev * 10) + rem
            x //= 10

        return Original == rev


