class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+" : lambda a,b : a + b,
            "-" : lambda a,b : b - a,
            "*" : lambda a,b : a * b,
            "/" : lambda a,b : int(b / a) 
        }
        res = None
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                res = ops[token](stack.pop(),stack.pop())
                stack.append(res)
        return stack.pop()
        
        