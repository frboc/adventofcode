package main


import (
	"os"
	"fmt"
	"strings"
)


func getData() (edges map[string][]string) {
	edges = make(map[string][]string)
	data, err := os.ReadFile("input.txt")
	if (err != nil) {
		panic(err)
	}
	for _, row := range strings.Split(string(data), "\r\n") {
		splited := strings.Split(row, ")")
		from, to := splited[0], splited[1]

		edges[from] = append(edges[from], to)
		edges[to] = append(edges[to], from)
	}
	return
}



func getRoads(edges map[string][]string, from string) (closedRoads [][]string) {
	openRoads := [][]string{[]string{from}}
	closedRoads = [][]string{}

	for len(openRoads) > 0 {
		road := openRoads[0]
		closedRoads = append(closedRoads, road)
		openRoads = openRoads[1:]

		lastEdge := road[len(road)-1]
		for _, nextEdge := range edges[lastEdge] {

			validRoad := true
			for _, edgeInRoad := range road {
				if edgeInRoad == nextEdge {
					validRoad = false
					break
				}
			}
			if !validRoad {
				continue
			}

			newRoad := make([]string, len(road)+1)
			copy(newRoad, road)
			newRoad[len(newRoad)-1] = nextEdge
			openRoads = append(openRoads, newRoad)
		}
	}
	return
}

func main() {
	edges := getData()

	closedRoads := getRoads(edges, "COM")
	sum := 0
	for _, road := range closedRoads {
		sum += len(road) - 1
	}
	fmt.Printf("Part 1: %v\n", sum)

	closedRoads = getRoads(edges, "YOU")

	var shortestRoad []string
	for _, road := range closedRoads {
		if road[len(road)-1] == "SAN" && (len(shortestRoad) == 0 || len(road) < len(shortestRoad)) {
			shortestRoad = road
		}
	}
	fmt.Printf("Part 2: %v\n", len(shortestRoad) - 3)
}