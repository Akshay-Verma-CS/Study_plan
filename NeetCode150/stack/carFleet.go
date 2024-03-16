import (
    "sort"
)

func carFleet(target int, position []int, speed []int) int {
    pairs := make([][2]float64, 0) 
    var stack []float64            

    for i := range position {
        pairs = append(pairs, [2]float64{float64(position[i]), float64(speed[i])})
    }

    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i][0] > pairs[j][0]
    })

    for _, pair := range pairs {
        time := (float64(target) - pair[0]) / pair[1]
        stack = append(stack, time)
        for len(stack) >= 2 && stack[len(stack)-1] <= stack[len(stack)-2] {
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack)
}