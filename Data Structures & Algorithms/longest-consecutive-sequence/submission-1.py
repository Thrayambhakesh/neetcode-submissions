class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        h={}

        if n==0:
            return 0
        for i in range(n):
            if nums[i]-1 not in h:
                h[nums[i]]=1
            else:

                h[nums[i]]=h[nums[i]-1]+1
        return max(h.values())
