package main

import "fmt"

// Facade
type Store struct {
	itemList []string	
}
func (s* Store) selectItems(itemList []string) {
	s.itemList = itemList
}
func (s* Store)buy() int {

	bucket := Bucket{}
	bucket.addItemList(s.itemList)
	itemList := bucket.getItemList()

	barcode := Barcode{}
	barcode.addTargetItemList(itemList)
	priceList := barcode.scanItemList()

	calculator := Calculator{}
	calculator.addPriceList(priceList)
	sum := calculator.calculatePriceList()
	fmt.Println(sum)

	return sum
}


// Subsystems
type Bucket struct {
	itemList []string
}
func (b* Bucket) addItemList(itemList []string) {
	for i := 0; i < len(itemList); i++ {
		b.itemList = append(b.itemList, itemList[i])
	}
}
func (b* Bucket) getItemList() []string {
	fmt.Println("바구니 안에 있는 제품들을 꺼냈습니다.")
	return b.itemList
}

type Barcode struct {
	targetItemList []string
}
func (b* Barcode) addTargetItemList(targetItemList []string) {
	for i := 0; i < len(targetItemList); i++ {
		b.targetItemList = append(b.targetItemList, targetItemList[i])
	}
}
func (b* Barcode) scanItemList() []int {
	fmt.Println("제품들을 바코드로 스캔합니다.")
	priceList := []int{}
	for i := 0; i < len(b.targetItemList); i++ {
		priceList = append(priceList, len(b.targetItemList[i]))
	}
	return priceList
}

type Calculator struct {
	priceList []int
}
func (c* Calculator) addPriceList(priceList []int) {
	fmt.Println("제품 가격을 나열합니다.")
	for i := 0; i < len(priceList); i++ {
		c.priceList = append(c.priceList, priceList[i])
	}
}
func (c* Calculator) calculatePriceList() int {
	fmt.Println("제품 가격을 계산합니다.")
	sum := 0
	for i := 0; i < len(c.priceList); i++ {
		sum += c.priceList[i]
	}
	return sum
}

type Client struct {
	selectedItemList []string
}
func (c* Client)buy() {
	store:= Store{c.selectedItemList}
	store.buy()

}

func main() {
	client := Client{[]string{"pen", "pencel", "keyboard", "computer"}}
	client.buy()
}