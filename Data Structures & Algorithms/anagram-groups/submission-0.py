class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h={}
        for i in strs:
            j="".join(sorted(i))
            if j in h:
                h[j].append(i)
            else:
                h[j]=[i]
        L=[]
        for x in h.values():
            L.append(x)
        return L
                
        
