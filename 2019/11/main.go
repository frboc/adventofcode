package main

import (
	"os"
	"strings"
	"strconv"
	"fmt"
	"math"
)

type Direction int
const (
	Up Direction = iota
	Right
	Down
	Left
)

func (d Direction) Rotate(r int) Direction {
	newD := int(d)
	if r == 0 {
		newD = newD - 1
		if newD < 0 {
			newD = 3
		}
	} else {
		newD = (newD + 1) % 4
	}
	return Direction(newD)
}

type Color int
const (
	Black Color = iota
	White
)

type Point struct {
	X int
	Y int
}

func (p *Point) Move(facing Direction) {
	switch facing{
	case Up:
		p.Y -= 1 
	case Right:
		p.X += 1
	case Down:
		p.Y += 1 
	case Left:
		p.X -= 1
	}
}

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

func solve(part2 bool) map[Point]int {
	data := getData()

	inputChan := make(chan int, 1)
	outputChan := make(chan int)

	go run(data, inputChan, outputChan)

	tiles := make(map[Point]int)
	facing := Up
	position := Point{0, 0}

	if part2 {
		tiles[Point{0, 0}] = int(White)
	}

	for {
		input := 0
		if val, ok := tiles[position]; ok {
		    input = val
		}
		inputChan <- input

		color, ok := <-outputChan
		if !ok {
			break
		}

		rotate := <-outputChan
		tiles[position] = color

		facing = facing.Rotate(rotate)
		position.Move(facing)
	}
	return tiles
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func plot(tiles map[Point]int) {
	minx, miny := math.MaxInt32, math.MaxInt32
	maxx, maxy := 0, 0 

	for point, _ := range tiles {
		minx = min(minx, point.X)
		maxx = max(maxx, point.X)
		miny = min(miny, point.Y)
		maxy = max(maxy, point.Y)
	}
	
	for j := miny; j <= maxy; j++ {
		for i := minx; i <= maxx; i++ {
			if val, ok := tiles[Point{i, j}]; ok && val == 1 {
				fmt.Print("*")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Println()
	}
}

func main() {
	fmt.Printf("Part 1: %v\n", len(solve(false)))
	fmt.Println("Part 2:")
	plot(solve(true))

}