package main

import "fmt"

type Printer struct {
	/*
		printedDataQueue: 프린트 대상의 문자열 큐
	*/
	printedData []string
}
func (p *Printer) addString(newString string) {
	p.printedData = append(p.printedData, newString)
}
func (p *Printer) print() bool {
	if len(p.printedData) == 0 {
		return false
	} else {
		targetPrint := p.printedData[0]
		p.printedData = p.printedData[1:]
		fmt.Println(targetPrint)
		return true
	}
}

var __instance *Printer = nil

func getPrinterInstance() *Printer {
	// Mutex 생략
	if __instance == nil {
		__instance = &Printer{}
		__instance.printedData = []string{}
	} else {
	}
	return __instance
}

func main() {
	printer1 := getPrinterInstance()
	printer2 := getPrinterInstance()

	printer1.addString("hello")
	printer2.addString("World")

	printer2.print()
	printer1.print()
}