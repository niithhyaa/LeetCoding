class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        minString=strs[0]
        for word in strs:
            if len(word)<len(minString):
                minString=word
        for i in range(len(minString)):
            for word in strs:
                if word[i]!=minString[i]:
                    return prefix
            prefix+=minString[i]
        return prefix
