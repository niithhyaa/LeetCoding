class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i<j):
                    if (nums[i]+nums[j] < target):
                        n+=1
        return n
