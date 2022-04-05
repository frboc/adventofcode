package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"math"
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

func getDigitFromInt(num int, position int) int {
    r := num % int(math.Pow(10, float64(position)))
    return r / int(math.Pow(10, float64(position-1)))
}

func getResult(data []int, input int) (result int) {
	numbers := make([]int, len(data))
	copy(numbers, data)

	var output int
	i := 0
	for {
		currentNumber := numbers[i]
		instruction := getDigitFromInt(currentNumber, 2) * 10 + getDigitFromInt(currentNumber, 1)
		modeA := getDigitFromInt(currentNumber, 3)
		modeB := getDigitFromInt(currentNumber, 4)
		// modeC := getDigitFromInt(currentNumber, 5)

		switch instruction {
		case 1, 2:
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}

			if instruction == 1 {
				numbers[numbers[i+3]] = a + b
			} else {
				numbers[numbers[i+3]] = a * b
			}
			i += 4
		case 3:
			numbers[numbers[i+1]] = input
			i += 2
		case 4:
			output = numbers[i+1]
			if modeA == 0 {
				output = numbers[output]
			}
			i += 2
		case 5:
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}
			if a != 0 {
				i = b
			} else {
				i += 3
			}
		case 6:
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}

			if a == 0 {
				i = b
			} else {
				i += 3
			}
		case 7:
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}

			if a < b {
				numbers[numbers[i+3]] = 1
			} else {
				numbers[numbers[i+3]] = 0
			}
			i += 4
		case 8: {
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}

			if a == b {
				numbers[numbers[i+3]] = 1
			} else {
				numbers[numbers[i+3]] = 0
			}
			i += 4
		}
		case 99:
			return output
		default:
			fmt.Println(instruction)
			panic("Unknown instruction")
		}
	}
}


func main() {
	numbers := getData()

	fmt.Printf("Part 1: %v\n", getResult(numbers, 1))
	fmt.Printf("Part 2: %v\n", getResult(numbers, 5))
}