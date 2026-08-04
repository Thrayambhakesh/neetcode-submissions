class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones)>1:

            m1=stones[-1]
            m2=stones[-2]
            if m1==m2:
                stones.pop()
                stones.pop()
            else:
                stones[-2]=stones[-1]-stones[-2]
                stones.pop()
                stones.sort()


        if len(stones)==0:
            return 0
        return stones[0]
            
                