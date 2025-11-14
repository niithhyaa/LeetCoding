class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans_arr = []
        arr = s.split()
        for i in range(k):
            ans_arr.append(arr[i])
        ans = " ".join(ans_arr)
        return ans
