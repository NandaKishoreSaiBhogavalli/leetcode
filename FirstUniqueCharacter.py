class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordcount = {}
        for char in s:
            wordcount[char] = wordcount.get(char, 0) + 1

        for index, char in enumerate(s):
            if wordcount[char] == 1:
                return index
        return -1


