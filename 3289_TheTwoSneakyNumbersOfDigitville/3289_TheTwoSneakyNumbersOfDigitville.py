class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        count = {}
        for x in nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
            if count[x] == 2:
                ans.append(x)
        return ans
