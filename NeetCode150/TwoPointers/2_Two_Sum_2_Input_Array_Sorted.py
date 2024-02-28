class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        front = 0
        rear = n - 1
        while front <= rear:
            currSum = numbers[front]+numbers[rear]
            if currSum == target:
                return [front+1,rear+1]
            elif currSum < target:
                front+=1
            else:
                rear-=1
        return []