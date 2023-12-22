package main

func main() {
	var test = "Hi"

	go func(test *string) {

	}(&test)
}
