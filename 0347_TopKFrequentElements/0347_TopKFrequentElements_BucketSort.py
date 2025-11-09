class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n]+=1
        buckets = [[] for i in range(len(nums)+1)]
        for num, freq in d.items():
            buckets[freq].append(num)
        ans = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
