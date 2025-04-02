class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word == word.capitalize() or word.isupper() or word.islower():
            return True
        return False