func twoSum(nums []int, target int) []int {
    complements := make(map[int]int)
    for index,element := range nums{
        
        if val,ok := complements[element];ok{
            return []int{val,index}
        }
        
        complements[target - element] = index
    }
    return nil
}