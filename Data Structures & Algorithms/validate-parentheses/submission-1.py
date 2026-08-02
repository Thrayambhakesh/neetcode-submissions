from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        q=deque()
        for i in s:
            if i==')':
                if len(q)==0 or q[-1]!='(':
                    return False
                else:
                    q.pop()
            elif i==']':
                if len(q)==0 or q[-1]!='[':
                    return False
                else:
                    q.pop()
            elif i=='}':
                if len(q)==0 or q[-1]!='{':
                    return False
                else:
                    q.pop()
            elif i=='(':
                q.append('(')
            elif i=='[':
                q.append('[')
            elif i=='{':
                q.append('{')
        if len(q)==0:
            return True
        else:
            return False
