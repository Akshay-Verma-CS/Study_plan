from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                curr = i
                currMax = 1
                while curr+1 in nums:
                    curr+=1
                    currMax+=1
                res = max(currMax,res)
        return res


        