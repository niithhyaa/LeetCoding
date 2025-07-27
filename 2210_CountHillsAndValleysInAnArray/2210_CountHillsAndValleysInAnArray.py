class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        result=0
        left=0
        right=-1
        for i in range(1,len(nums)-1):
            if nums[i-1]==nums[i]:
                continue
            #left nearest non-equal neighbour
            for j in range(i-1,-1,-1):
                if nums[j]!=nums[i]:
                    left=j
                    break
            #right nearest non-equal neighbour
            for j in range(i+1,len(nums)):
                if nums[j]!=nums[i]:
                    right=j
                    break
            
            if (nums[left]<nums[i]) and (nums[right]<nums[i]):
                result+=1
            if (nums[left]>nums[i]) and (nums[right]>nums[i]):
                result+=1
        return result
