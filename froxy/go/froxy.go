package main
import "fmt"

// Subject
type Payment interface {
	do_pay() bool
}
// RealSubject
type Bank struct {
	card string
	account string
}
func (b* Bank) __getAccount() string {
	b.account = b.card
	return b.account
}
func (b* Bank) __hasFunds() bool {
	fmt.Printf("Bank:: Checking if Account, %s has enough funds\n", b.__getAccount())
	return true
}
func (b* Bank) setCard(card string) {
	b.card = card
}
func (b* Bank) do_pay() bool {
	if b.__hasFunds() {
		fmt.Println("Bank:: Paying the merchant")
		return true
	} else {
		fmt.Println("Bank:: Sorry, not enough funds!")
		return false
	}
}

// Froxy
type Debitcard struct {
	bank Bank
}
func (d* Debitcard) do_pay() bool {
	card := ""
	fmt.Printf("Proxy:: Punch in Card Number: ")
	fmt.Scan(&card)
	d.bank.setCard(card)
	return d.bank.do_pay()
}

// init function
func initDebitCard() Debitcard {
	return Debitcard{Bank{"", ""}}
}

// client
type Client struct {
	debitCard Debitcard
	isPurchased bool
}

func (c* Client) makePayment() {
	c.isPurchased = c.debitCard.do_pay()
}
func (c* Client) getResult() {
	if c.isPurchased {
		fmt.Println("Denim Shirt is Mine")
	} else {
		fmt.Println("I should earn more")
	}
}

// init client function
func initClient() Client {
	fmt.Println("Let's buy denim shirt")
	return Client{initDebitCard(), false}
}
func main() {
	var c Client = initClient()
	c.makePayment()
	c.getResult()
}