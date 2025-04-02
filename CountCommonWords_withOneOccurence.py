class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        wordcount1 = {}
        wordcount2 = {}

        for word in words1:
            wordcount1[word] = wordcount1.get(word, 0) + 1

        for word in words2:
            wordcount2[word] = wordcount2.get(word, 0) + 1
        count = 0
        for key in wordcount1:
            if wordcount1[key] == 1 and wordcount2.get(key, 0) == 1:
                count += 1

        return count