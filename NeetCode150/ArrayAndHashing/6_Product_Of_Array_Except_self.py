class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [ 0 for i in range(n)]
        forward[0] = nums[0]

        for i in range(1,n):
            forward[i] = forward[i-1]*nums[i]
        backward = [ 0 for i in range(n)]
        backward[-1] = nums[-1]

        for i in reversed(range(0,n-1)):
            backward[i] = backward[i+1]*nums[i]
        ans = [ 0 for i in range(n)]
        ans[0] = backward[1]
        ans[-1] = forward[-2]
        for i in range(1,n-1):
            ans[i] = forward[i-1]*backward[i+1]
        return ans