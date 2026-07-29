class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L=[]
        if nums.count(0)>=2:
            return [0]*len(nums)
        elif nums.count(0)==1:
            idx=nums.index(0)
            p=1
            for i in range(idx):
                p*=nums[i]
            for i in range(idx+1,len(nums)):
                p*=nums[i]
            
            for i in range(idx):
                L.append(0)
            L.append(p)
            for i in range(len(nums)-idx-1):
                L.append(0)
        else:
            p=1
            for i in range(len(nums)):
                p*=nums[i]
            for i in range(len(nums)):
                L.append(p//nums[i])
        return L


