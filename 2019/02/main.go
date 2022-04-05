package main

import(
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getData() (numbers []int) {
	data, err := os.ReadFile("input.txt")
	if (err != nil) {
		panic(err)
	}
	for _, num := range strings.Split(string(data), ",") {
		n, _ := strconv.Atoi(num)
		numbers = append(numbers, n)
	}
	return
}

func getResult(data []int, noun int, verb int) (result int) {
	numbers := make([]int, len(data))
	copy(numbers, data)

	numbers[1] = noun
	numbers[2] = verb
	i := 0
	for {
		currentNumber := numbers[i]
		if (currentNumber == 1) {
			numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
			i += 4
		} else if (currentNumber == 2) {
			numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]
			i += 4
		} else if (currentNumber == 99) {
			result = numbers[0]
			return
		} else {
			panic("Unknown state")
		}
	}
}

func main() {
	numbers := getData()

	part2result := 0
	for i := 0; i <= 100; i++ {
		for j := 0; j <= 100; j++ {
			res := getResult(numbers, i, j)
			if res == 19690720 {
				part2result = 100 * i + j
				break
			}
		}
	}

	fmt.Printf("Part 1: %v\n", getResult(numbers, 12, 2))
	fmt.Printf("Part 2: %v\n", part2result)
}