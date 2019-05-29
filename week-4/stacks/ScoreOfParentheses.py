class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        if not S: return 0
        
        combo = 0
        stack = []
        for c in S:
            if c == '(':            
                stack.append(c)
            else:
                left = stack.pop(-1)
                if left == '(':
                    stack.append(1)
                else:
                    tot = 0
                    while left != '(':
                        tot += int(left)
                        left = stack.pop(-1)
                    stack.append(2 * tot)
        
        return sum(stack)