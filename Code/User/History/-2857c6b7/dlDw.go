package main

import (
	"log"
)

func main() {
	var test = "Hi"

	go func(test *string) {
		for {
			log.Println(*test)
		}
	}(&test)

	test = "Hi2"

	for {
	}
}
