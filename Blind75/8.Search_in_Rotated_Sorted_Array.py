class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target: 
                return 0 
            else:
                return -1
        if nums[0] < nums[-1]:
            return self.binarySearch(nums,0,len(nums)-1,target)
        for i in range(0,len(nums)-1):
            if nums[i] == target:
                return i
            if nums[i] > nums[i+1]:
                return self.binarySearch(nums,i+1,len(nums)-1,target)

    
    def binarySearch(self,nums, low , high , target):
        if high > len(nums):
            return -1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1