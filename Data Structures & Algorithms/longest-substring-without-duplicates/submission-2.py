class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        maxi=0
        n=len(s)
        l=0
        r=0
        c=0
        while r<n:
            if s[r] not in s1:
                s1.add(s[r])
                c+=1
                maxi=max(maxi,c)
            else:
                while s[r] in s1:
                    
                    s1.remove(s[l])
                    l+=1
                    c-=1
                s1.add(s[r])
                c+=1
                maxi=max(maxi,c)

            r+=1
        return maxi

                
                


                
