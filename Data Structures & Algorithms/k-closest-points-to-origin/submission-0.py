import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        L=[]
        L2=[]
        for i in points:
            a,b=i
            dist=math.sqrt(math.pow(a,2)+math.pow(b,2))
            L2.append(dist)
        
        L3=[]
        for i in range(k):
            maxi=min(L2)
            idx=L2.index(maxi)
            L2[idx]=1000
            L3.append(points[idx])
        
        return L3
