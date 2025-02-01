class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        current_max_here = nums[0]
        for i in range(1,len(nums)):
            temp = current_max_here + nums[i]
            if temp < nums[i]:
                current_max_here = nums[i]
            else:
                current_max_here = temp
            if current_max_here > maxSum:
                maxSum = current_max_here
        return maxSum