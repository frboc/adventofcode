package main

import (
	"os"
	"strings"
	"strconv"
	"fmt"
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

func main() {
	data := getData()
	
	fmt.Printf("Part 1: %v\n", run(data, 1))
	fmt.Printf("Part 2: %v\n", run(data, 2))
	
}