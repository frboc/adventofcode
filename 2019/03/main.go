package main

import(
	"strings"
	"os"
	"fmt"
	"strconv"
)

func getData() (wires [2][]string) {
	data, err := os.ReadFile("input.txt")
	if (err != nil) {
		panic(err)
	}
	lines := strings.Split(string(data), "\r\n")
	wires = [2][]string{strings.Split(lines[0], ","), strings.Split(lines[1], ",")}
	return
}

type Point struct {
	x int
	y int
}

func getPoints(from Point, x, y, steps int) (points []Point) {
	for i := 1; i <= steps; i++ {
		keyx := from.x + x * i
		keyy := from.y + y * i
		points = append(points, Point{x: keyx, y: keyy})
	}
	return
}

func getWirePoints(wire []string) (points map[Point]bool) {
	points = make(map[Point]bool)
	points[Point{0, 0}] = true
	currentPosition := Point{0, 0}

	for _, command := range wire {
		direction := command[0]
		steps, _ := strconv.Atoi(command[1:])

		x, y := 0, 0
		switch direction {
		case 'U':
			y = 1
		case 'D':
			y = -1
		case 'L':
			x = -1
		case 'R':
			x = 1
		default:
			panic("Unknown direction")			
		}
		newPoints := getPoints(currentPosition, x, y, steps)
		currentPosition = newPoints[len(newPoints)-1]
		for _, point := range newPoints {
			points[point] = true
		}
	}
	return
}

func countDistance(point Point) (distance int) {
	x := point.x
	if x < 0 {
		x = x * -1
	}
	y := point.y
	if y < 0 {
		y = y * -1
	}
	return x + y
}

func getLengthToTarget(wire []string, target Point) (counter int) {
	currentPosition := Point{0, 0}
	counter = 0


	for _, command := range wire {
		direction := command[0]
		steps, _ := strconv.Atoi(command[1:])

		x, y := 0, 0
		switch direction {
		case 'U':
			y = 1
		case 'D':
			y = -1
		case 'L':
			x = -1
		case 'R':
			x = 1
		default:
			panic("Unknown direction")
		}
		newPoints := getPoints(currentPosition, x, y, steps)
		currentPosition = newPoints[len(newPoints)-1]
		for _, point := range newPoints {
			counter++
			if point == target {
				return
			}
		}
	}
	panic("Something went wrong")
}


func main() {
	wires := getData()
	points1 := getWirePoints(wires[0])
	points2 := getWirePoints(wires[1])

	intersections := make(map[Point]bool)
	shortestDistance := 2147483647
	for point1 := range points1 {
		if point1.x == 0 && point1.y == 0 {
			continue
		}
		if p := points2[point1]; !p {
		    continue
		}
		intersections[point1] = true
		distance := countDistance(point1)
		if distance < shortestDistance {
			shortestDistance = distance
		}
	}
	fmt.Printf("Part 1: %v\n", shortestDistance)

	bestResult := 2147483647
	for target, _ := range intersections {
		length1 := getLengthToTarget(wires[0], target)
		length2 := getLengthToTarget(wires[1], target)

		if length1 + length2 < bestResult {
			bestResult = length1 + length2
		}
	}
	fmt.Printf("Part 2: %v\n", bestResult)
}