package main

import (
	"fmt"
	"os"
	"bufio"
	"strconv"
	"flag"
)

func getInputFileName() (fileName string) {
	testFlagPointer := flag.Bool("t", false, "Use test file")
	flag.Parse()

	if (*testFlagPointer) {
		fileName = "test_input.txt"
	} else {
		fileName = "input.txt"
	}
	return
}

func getData(fileName string) (lines []uint) {
	file, err := os.Open(fileName)
	if (err != nil) {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line, _ := strconv.Atoi(scanner.Text())
		lines = append(lines, uint(line))
	}
	return
}

func calculateFuel(mass uint, recursively bool) (fuel uint) {
	f := int(mass) / 3 - 2
	if (f <= 0) {
		f = 0
	}
	fuel = uint(f)
	if (!recursively || fuel == 0) {
		return
	}
	fuel += calculateFuel(fuel, true)
	return
}

func main() {
	fileName := getInputFileName()
	var sumPart1 uint = 0
	var sumPart2 uint = 0
	for _, val := range getData(fileName) {
		sumPart1 += calculateFuel(val, false)
		sumPart2 += calculateFuel(val, true)
	}
	fmt.Printf("Part 1: %v\n", sumPart1)
	fmt.Printf("Part 2: %v\n", sumPart2)
}