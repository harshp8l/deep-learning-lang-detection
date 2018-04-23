package main

import "fmt"

func main() {
    values := [][]int{}

    // These are the first two rows.
    row1 := []int{1, 2, 3}
    row2 := []int{4, 5, 6}
    row3 := []int{7, 8, 9}

    // Append each row to the two-dimensional slice.
    values = append(values, row1)
    values = append(values, row2)
    values = append(values, row3)


    fmt.Println(getPermutation(values))
}

func getPermutation(vids [][]int) [][]int {
    toRet := [][]int{}

    if len(vids) == 0 {
      return toRet
    }

    if len(vids) == 1 {
        for _, vid := range vids[0] {
            toRet = append(toRet, []int{vid})
        }
        return toRet
    }

    t := getPermutation(vids[1:])
    for _, vid := range vids[0] {
        for _, perm := range t {
            toRetAdd := append([]int{vid}, perm...)
            toRet = append(toRet, toRetAdd)
        }
    }

    return toRet
}
