class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=0
            d[nums[i]]+=1
        n = 0
        ans = []
        maximum = 0
        maxkey = 0
        while n<k:
            maximum = 0
            maxkey = 0
            for key, value in d.items():
                if value>maximum:
                    maximum = value
                    maxkey = key
            ans.append(maxkey)
            d.pop(maxkey)
            n+=1
        return ans
            
