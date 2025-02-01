class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [nums[0]]*n
        r = [nums[-1]]*n
        for i in range(1,n):
            l[i] = l[i-1]*nums[i]
        for i in reversed(range(0,n-1)):
            r[i] = r[i+1]*nums[i]
        ans = [0]*n
        ans[0] = r[1]
        ans[-1] = l[-2]
        for i in range(1,n-1):
            ans[i] = l[i-1]*r[i+1]
        return ans