package main

import "fmt"

func fib() func() int {
	a := 0
	b := 1
	c := 0
	return func() int {
		c = a + b
		a, b = b, c
		return b
	}
}

func main() {
	f := fib()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
