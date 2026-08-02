from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q=deque()
        if len(tokens)==0:
            return 0
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            if i not in ['-','+','/','*']:
                q.append(i)
            elif i =='+':
                a=q.pop()
                b=q.pop()
                q.append(int(a)+int(b))
            elif i =='*':
                a=q.pop()
                b=q.pop()
                q.append(int(a)*int(b))
            elif i =='/':
                b=q.pop()
                a=q.pop()
                q.append(int(float(a)/float(b)))
            elif i =='-':
                b=q.pop()
                a=q.pop()
                q.append(int(a)-int(b))
        return q[-1]
                
