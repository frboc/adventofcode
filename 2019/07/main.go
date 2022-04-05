package main

import(
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

func permutations(arr []int)[][]int{
    var helper func([]int, int)
    res := [][]int{}

    helper = func(arr []int, n int){
        if n == 1{
            tmp := make([]int, len(arr))
            copy(tmp, arr)
            res = append(res, tmp)
        } else {
            for i := 0; i < n; i++{
                helper(arr, n - 1)
                if n % 2 == 1{
                    tmp := arr[i]
                    arr[i] = arr[n - 1]
                    arr[n - 1] = tmp
                } else {
                    tmp := arr[0]
                    arr[0] = arr[n - 1]
                    arr[n - 1] = tmp
                }
            }
        }
    }
    helper(arr, len(arr))
    return res
}


func solve(data []int, phaseValues []int) (maxOutput int) {
	for _, phase := range permutations(phaseValues) {
		n := len(phase)
		ch := make([]chan int, n)
		for i := 0; i < n; i++ {
			ch[i] = make(chan int, 100)
			ch[i]<-phase[i]
		}
		ch[n-1] <- 0
		chExit := make(chan bool)
		for i := 0; i < n; i++ {
			if i == 0 {
				go intCodeRun(data, ch[n-1], ch[i], chExit)
			} else {
				go intCodeRun(data, ch[i-1], ch[i], chExit)
			}
		}

		<-chExit

		val := <-ch[4]
		if val > maxOutput {
			maxOutput = val
		}
	}

	return 
}

func main() {
	data := getData()



	phaseValues := []int{0,1,2,3,4}
	fmt.Printf("Part 1: %v\n", solve(data, phaseValues))
	phaseValues = []int{5,6,7,8,9}
	fmt.Printf("Part 2: %v\n", solve(data, phaseValues))
}