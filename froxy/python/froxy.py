from abc import ABCMeta, abstractmethod

# Subject
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass
# RealSubject
class Bank(Payment):
    
    def __init__(self):
        self.card = None
        self.account = None
    
    def __getAccount(self):
        self.account = self.card
        return self.account

    def __hasFunds(self):
        print("Bank:: Checking if Account", self.__getAccount(), "has enough funds")
        return True
    
    def setCard(self, card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: Paying the merchant")
            return True
        else:
            print("Bank:: Sorry, not enough funds!")
            return False

# Froxy
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()

# Client
class Client:
    def __init__(self):
        print("You:: Let's buy Denim shirt")
        self.debitCard = DebitCard()
        self.isPurchased = None
    
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("Denim Shirt is mine")
        else:
            print("I should earn more")    

if __name__ == "__main__":
    c = Client()
    c.make_payment()
    del c