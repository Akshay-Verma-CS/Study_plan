class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n == 1: return [0]
        ans = [0]*n
        stack = [n-1]
        for i in range(n-2,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]-i
            stack.append(i)
        return ans

        