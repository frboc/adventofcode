package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Vector struct {
	X, Y, Z int
}

type Moon struct {
	Pos, Vel Vector
}

func getData() (moons []Moon) {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	for _, row := range strings.Split(string(data), "\r\n") {
		splited := strings.Split(row, "=")
		x := strings.Trim(splited[1], ", y")
		y := strings.Trim(splited[2], ", z")
		z := strings.Trim(splited[3], ">")
		a, _ := strconv.Atoi(x)
		b, _ := strconv.Atoi(y)
		c, _ := strconv.Atoi(z)
		pos := Vector{a, b, c}
		vel := Vector{0, 0, 0}
		moons = append(moons, Moon{pos, vel})
	}
	return
}

func absInt(a int) int {
	if a > 0 {
		return a
	}
	return a * -1
}

func updatePositionOfMoons(moons []Moon) {
	for i, _ := range moons {
		for j, _ := range moons {
			if i == j {
				continue
			}
			if moons[i].Pos.X < moons[j].Pos.X {
				moons[i].Vel.X++
			}
			if moons[i].Pos.Y < moons[j].Pos.Y {
				moons[i].Vel.Y++
			}
			if moons[i].Pos.Z < moons[j].Pos.Z {
				moons[i].Vel.Z++
			}
			if moons[i].Pos.X > moons[j].Pos.X {
				moons[i].Vel.X--
			}
			if moons[i].Pos.Y > moons[j].Pos.Y {
				moons[i].Vel.Y--
			}
			if moons[i].Pos.Z > moons[j].Pos.Z {
				moons[i].Vel.Z--
			}
		}
	}

	for i, _ := range moons {
		moons[i].Pos.X += moons[i].Vel.X
		moons[i].Pos.Y += moons[i].Vel.Y
		moons[i].Pos.Z += moons[i].Vel.Z
	}
}

func solvePart1() (result int) {
	moons := getData()

	for x := 0; x < 2772; x++ {
		updatePositionOfMoons(moons)
	}

	for _, moon := range moons {
		pot := absInt(moon.Pos.X) + absInt(moon.Pos.Y) + absInt(moon.Pos.Z)
		kin := absInt(moon.Vel.X) + absInt(moon.Vel.Y) + absInt(moon.Vel.Z)
		result += pot * kin
	}
	return
}

func isXSame(moons1, moons2 []Moon) bool {
	for i := 0; i < len(moons1); i++ {
		if moons1[i].Pos.X != moons2[i].Pos.X {
			return false
		}
		if moons1[i].Vel.X != moons2[i].Vel.X {
			return false
		}
	}
	return true
}

func isYSame(moons1, moons2 []Moon) bool {
	for i := 0; i < len(moons1); i++ {
		if moons1[i].Pos.Y != moons2[i].Pos.Y {
			return false
		}
		if moons1[i].Vel.Y != moons2[i].Vel.Y {
			return false
		}
	}
	return true
}

func isZSame(moons1, moons2 []Moon) bool {
	for i := 0; i < len(moons1); i++ {
		if moons1[i].Pos.Z != moons2[i].Pos.Z {
			return false
		}
		if moons1[i].Vel.Z != moons2[i].Vel.Z {
			return false
		}
	}
	return true
}

func greatestCommonDivisor(a, b int) int {
	for b > 0 {
		temp := b
		b = a % b
		a = temp
	}
	return a
}

func leastCommonMultiple(a, b int) int {
	return (a * b) / greatestCommonDivisor(a, b)
}

func solvePart2() int {
	moons := getData()
	moonsStartingPosition := make([]Moon, len(moons))
	copy(moonsStartingPosition, moons)

	var cycleX, cycleY, cycleZ int
	i := 0
	for {
		i++
		updatePositionOfMoons(moons)

		if cycleX == 0 && isXSame(moons, moonsStartingPosition) {
			cycleX = i
		}
		if cycleY == 0 && isYSame(moons, moonsStartingPosition) {
			cycleY = i
		}
		if cycleZ == 0 && isZSame(moons, moonsStartingPosition) {
			cycleZ = i
		}

		if cycleX != 0 && cycleY != 0 && cycleZ != 0 {
			break
		}
	}
	return leastCommonMultiple(cycleX, leastCommonMultiple(cycleY, cycleZ))
}

func main() {
	fmt.Printf("Part 1: %v\n", solvePart1())
	fmt.Printf("Part 2: %v\n", solvePart2())
}
