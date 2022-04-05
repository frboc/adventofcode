package main

import (
	"fmt"
	"strconv"
)

const MIN = 183564
const MAX = 657474

func isValid(pass string, excludeLargeGroups bool) bool {
	valid := false
	for i := 0; i < len(pass)-1; i++ {
		a, _:= strconv.Atoi(string(pass[i]))
		b, _ := strconv.Atoi(string(pass[i+1]))

		if !excludeLargeGroups {	
			if a == b {
				valid = true
			}
		} else {
			x, y := -1, -1
			if i != len(pass) - 2 {
				x, _ = strconv.Atoi(string(pass[i+2]))
			} 
			if i != 0 {
				y, _ = strconv.Atoi(string(pass[i-1]))
			}
			if a != x && a == b && b != y {
				valid = true
			}
		}

		if a > b {
			return false
		}
	}
	return valid
}


func main() {
	counter1, counter2 := 0, 0
	for i := MIN; i <= MAX; i++ {
		if isValid(strconv.Itoa(i), false) {
			counter1++
		}
		if isValid(strconv.Itoa(i), true) {
			counter2++
		}
	}
	fmt.Printf("Part 1: %v\n", counter1)
	fmt.Printf("Part 2: %v\n", counter2)
}