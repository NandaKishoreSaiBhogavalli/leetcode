class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        wordcount = {}

        for char in s:
            wordcount[char] = wordcount.get(char, 0) + 1

        for char in t:
            if char not in wordcount or wordcount[char] == 0:
                return False
            wordcount[char] -= 1

        return True
