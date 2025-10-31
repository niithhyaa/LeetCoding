class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_list = list(allowed)
        res = 0
        for i in range(len(words)):
            c=0
            for j in words[i]:
                if j not in allowed_list:
                    c+=1
                    break
            if c==0:
                res+=1
        return res
