package main

import (
	"os"
	"strconv"
	// "strings"
	"fmt"
)

// const X = 2
// const Y = 2
const X = 6
const Y = 25

func getData() string {
	data, err := os.ReadFile("input.txt")
	if (err != nil) {
		panic(err)
	}
	return string(data)
}

func parseToLayers(input string) [][X][Y]int {
	nLayers := len(input) / (X * Y)
	layers := make([][X][Y]int, nLayers)

	l := 0
	for i := 0; i < nLayers; i++ {
		for j := 0; j < X; j++ {
			for k := 0; k < Y; k++ {
				var err error
				layers[i][j][k], err = strconv.Atoi(string(input[l]))
				if err != nil {
					panic(err)
				}
				l++
			}
		}	
	}

	return layers
}

func countDigitsInLayer(layer [X][Y]int, digit int) (counter int) {
	for _, row := range layer {
		for _, el := range(row) {
			if el == digit {
				counter++
			}
		}
	}
	return
}


func getFinalImage(layers [][X][Y]int) (finalImage [X][Y]int) {
	for i := 0; i < X; i++ {
		for j := 0; j < Y; j++ {
			for k := 0; k < len(layers); k++ {
				if layers[k][i][j] != 2 {
					finalImage[i][j] = layers[k][i][j]
					// fmt.Print(layers[k][i][j])
					break
				}
			}
		}
	}
	return
}



func main() {
	data := getData()
	layers := parseToLayers(data)

	var bestLayer [X][Y]int
	bestLayerNZeros := 2147483647
	for _, layer := range layers {
		nZeros := countDigitsInLayer(layer, 0)
		if nZeros < bestLayerNZeros {
			bestLayerNZeros = nZeros
			bestLayer = layer
		}
	}



	res1 := countDigitsInLayer(bestLayer, 1) * countDigitsInLayer(bestLayer, 2)
	fmt.Printf("Part 1: %v\n", res1)

	fmt.Println("Part 2:")
	finalImage := getFinalImage(layers)
	for _, row := range finalImage {
		for _, ch := range row {
			if ch == 1 {
				fmt.Print("*")
			} else {
				fmt.Print(" ")
			}
		}
		fmt.Print("\n")
	}
}