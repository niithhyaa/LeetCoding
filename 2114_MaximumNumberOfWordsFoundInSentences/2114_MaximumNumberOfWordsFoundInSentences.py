class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = 0
        for sentence in sentences:
            x = len(sentence.split(" "))
            if x>maximum:
                maximum = x
        return maximum
