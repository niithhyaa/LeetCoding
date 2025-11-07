class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = [0]*(len(A)+1)
        count = 0
        res = []
        for i in range(len(A)-1):
            freq[A[i]] += 1
            if (freq[A[i]]==2):
                count = count+1
            freq[B[i]] += 1
            if (freq[B[i]]==2):
                count = count+1
            res.append(count)
        res.append(len(A))
        return res
