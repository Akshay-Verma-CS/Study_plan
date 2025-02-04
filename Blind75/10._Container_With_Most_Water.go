package blind75

func maxArea(height []int) int {
	var n int = len(height)
	var leftPointer int = 0
	var rightPointer int = n - 1
	var Area, M int
	for leftPointer < rightPointer {
		Area = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
		M = max(Area, M)
		if height[leftPointer] < height[rightPointer] {
			leftPointer++
		} else {
			rightPointer--
		}
	}
	return M
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}
