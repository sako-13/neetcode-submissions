import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == '+':
                right = s.pop()
                left = s.pop()
                s.append(int(left+right))
            elif i == '-':
                right = s.pop()
                left = s.pop()
                s.append(int(left-right))
            elif i == '*':
                right = s.pop()
                left = s.pop()
                s.append(int(left*right))
            elif i == '/':
                right = s.pop()
                left = s.pop()
                s.append(int(left/right))
            else:
                s.append(int(i))
        return int(s[0])