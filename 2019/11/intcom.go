package main

import (
	"fmt"
	"math"
)

func getDigitFromInt(num int, position int) int {
    r := num % int(math.Pow(10, float64(position)))
    return r / int(math.Pow(10, float64(position-1)))
}

func run(data []int, inputChan, outputChan chan int) {
	numbers := make([]int, 10000)
	copy(numbers, data)

	relativeBase := 0

	i := 0
	for {
		currentNumber := numbers[i]
		instruction := getDigitFromInt(currentNumber, 2) * 10 + getDigitFromInt(currentNumber, 1)
		modeA := getDigitFromInt(currentNumber, 3)
		modeB := getDigitFromInt(currentNumber, 4)
		modeC := getDigitFromInt(currentNumber, 5)
		// if modeC != 0 {
		// 	fmt.Println("modeC", currentNumber)
		// }

		// fmt.Println(i, numbers[i], numbers[i+1], numbers[i+2], relativeBase)

		switch instruction {
		case 1, 2:
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			if modeA == 2 {
				x := numbers[i+1]
				a = numbers[relativeBase+x]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}
			if modeB == 2 {
				x := numbers[i+2]
				b = numbers[relativeBase+x]
			}
			c := numbers[i+3]
			if modeC == 2 {
				x := numbers[i+3]
				c = relativeBase+x
			}

			if instruction == 1 {
				numbers[c] = a + b
			} else {
				numbers[c] = a * b
			}
			i += 4
		case 3:
			input := <-inputChan
			if modeA == 0 {
				numbers[numbers[i+1]] = input
			}
			if modeA == 2 {
				x := numbers[i+1]
				numbers[relativeBase+x] = input
			}
			if modeA == 1 {
				panic("asdf")
			}
			i += 2
		case 4:
			out := numbers[i+1]
			if modeA == 0 {
				out = numbers[out]
			}
			if modeA == 2 {
				x := numbers[i+1]
				out = numbers[relativeBase+x]
			}
			outputChan <- out
			i += 2
		case 5, 6:
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			if modeA == 2 {
				x := numbers[i+1]
				a = numbers[relativeBase+x]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}
			if modeB == 2 {
				x := numbers[i+2]
				b = numbers[relativeBase+x]
			}
			if instruction == 5 && a != 0 {
				i = b
			} else if instruction == 6 && a == 0 {
				i = b
			} else {
				i += 3
			}
		case 7:
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			if modeA == 2 {
				x := numbers[i+1]
				a = numbers[relativeBase+x]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}
			if modeB == 2 {
				x := numbers[i+2]
				b = numbers[relativeBase+x]
			}
			c := numbers[i+3]
			if modeC == 2 {
				x := numbers[i+3]
				c = relativeBase+x
			}

			if a < b {
				numbers[c] = 1
			} else {
				numbers[c] = 0
			}
			i += 4
		case 8: {
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			if modeA == 2 {
				x := numbers[i+1]
				a = numbers[relativeBase+x]
			}
			b := numbers[i+2]
			if modeB == 0 {
				b = numbers[b]
			}
			if modeB == 2 {
				x := numbers[i+2]
				b = numbers[relativeBase+x]
			}
			c := numbers[i+3]
			if modeC == 2 {
				x := numbers[i+3]
				c = relativeBase+x
			}

			if a == b {
				numbers[c] = 1
			} else {
				numbers[c] = 0
			}
			i += 4
		}
		case 9: {
			a := numbers[i+1]
			if modeA == 0 {
				a = numbers[a]
			}
			if modeA == 2 {
				x := numbers[i+1]
				a = numbers[relativeBase+x]
			}
			relativeBase += a
			i += 2
		}
		case 99:
			close(outputChan)
			return
		default:
			fmt.Println(instruction)
			panic("Unknown instruction")
		}
	}
}
