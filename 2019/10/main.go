package main

import (
	"os"
	"strings"
	"fmt"
	"math"
	"sort"
)

const float64EqualityThreshold = 1e-9

type Asteroid struct {
	X, Y int
}

type AsteroidRelativePosition struct {
	a Asteroid
	angle float64
	distance float64
	removed bool
}

type AsteroidsByAngle []AsteroidRelativePosition

func (a AsteroidsByAngle) Len() int {
	return len(a)
}

func (a AsteroidsByAngle) Less(i, j int) bool{
	return a[i].angle < a[j].angle
}

func (a AsteroidsByAngle) Swap(i, j int) {
	a[i], a[j] = a[j], a[i]
}

func getClosestByAngle(asteroids AsteroidsByAngle, angle float64) (closest AsteroidRelativePosition) {
	for _, a := range asteroids {
		if a.removed {
			continue
		}
		if math.Abs(a.angle - angle) > float64EqualityThreshold  {
			continue
		}
		if closest != (AsteroidRelativePosition{}) && closest.distance < a.distance {
			continue
		}
		closest = a
	}
	return 
}


func (a1 *Asteroid) getAngle(a2 Asteroid) (angle float64) {
	a := float64(a2.X - a1.X)
	b := float64(a2.Y - a1.Y)
	c := a1.getDistance(a2)

	b = b * -1
	if a >= 0 && b >= 0 {
		angle = math.Asin(float64(a) / c)
	}
	if a >= 0 && b < 0 {
		angle = math.Asin(float64(b*-1) / c)
		angle += math.Pi / 2
	}
	if a < 0 && b < 0 {
		angle = math.Asin(float64(a*-1) / c)
		angle += math.Pi
	}
	if a < 0 && b >= 0 {
		angle = math.Asin(float64(b) / c)
		angle += (math.Pi / 2) * 3
	}

	return
}

func (a1 *Asteroid) getDistance(a2 Asteroid) float64 {
	a := float64(a2.X - a1.X)
	b := float64(a2.Y - a1.Y)
	return math.Sqrt(math.Pow(a, 2.0) + math.Pow(b, 2.0))
}

func (a1 *Asteroid) sortByAngle(asteroids []Asteroid) (result []AsteroidRelativePosition) {
	for _, a := range asteroids {
		if a == *a1 {
			continue
		}
		result = append(result, AsteroidRelativePosition{a, a1.getAngle(a), a1.getDistance(a), false})
	}
	sort.Sort(AsteroidsByAngle(result))
	return
}

func getData() (data []Asteroid) {
	input, err := os.ReadFile("input.txt")
	if (err != nil) {
		panic(err)
	}
	for i, row := range strings.Split(string(input), "\n") {
		for j, ch := range row {
			if ch == '#' {
				data = append(data, Asteroid{j, i})
			}
		}
	}
	return
}

func main() {
	data := getData()

	best := 0
	var bestAsteroid Asteroid 
	for _, a1 := range data {
		seen := make(map[float64]bool)
		for _, a2 := range data {
			if a1 == a2 {
				continue
			}
			angle := a1.getAngle(a2)
			inMap := false
			for a, _ := range seen {
				if math.Abs(a - angle) <= float64EqualityThreshold {
					inMap = true
					break
				}
			}
			if !inMap {
				seen[angle] = true
			}
		}

		if len(seen) > best {
			best = len(seen)
			bestAsteroid = a1
		}
	}
	fmt.Printf("Part 1: %v\n", best)

	otherRelative := bestAsteroid.sortByAngle(data)
	var part2 AsteroidRelativePosition
	lastAngle := 99.0
	i := 0
	Exit:
	for {
		for _, x := range otherRelative {
			if x.removed == true {
				continue
			}
			if math.Abs(lastAngle - x.angle) <= float64EqualityThreshold {
				continue
			}
			i++
			a := getClosestByAngle(otherRelative, x.angle)
			a.removed = true

			if i == 200 {
				part2 = a
				break Exit
			}
			lastAngle = a.angle
		}
	}
	part2result := part2.a.X * 100 + part2.a.Y
	fmt.Printf("Part 2: %v\n", part2result)
}