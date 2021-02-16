# Facade
class Store:
    def __init__(self):
        pass
    def buy(self, item_list):
        item_list = Bucket(item_list)()
        price_list = Barcode(item_list)()
        price = Calculator(price_list)()

        print(f"가격은 {price} 입니다.")

# Subsystems
class Bucket:
    def __init__(self, item_list):
        self.item_list = []
        for item in item_list:
            self.item_list.append(item)

    def __call__(self):
        print("바구니 안에 있는 제품들을 꺼냈습니다.")
        print("")
        return self.item_list

class Barcode:
    def __init__(self, item_list):
        print("제품들을 진열대 위에 올려놓았습니다.")
        self.target_item_list = []
        for item in item_list:
            self.target_item_list.append(item)

    def __call__(self):
        price_list = []
        print("제품들을 바코드로 스캔합니다.")
        for item in self.target_item_list:
            print(item)
            price_list.append(len(item))
        print("")
        return price_list

class Calculator:
    def __init__(self, price_list):
        print("제품 가격을 나열합니다.")
        self.price_list = []
        for item in price_list:
            self.price_list.append(item)

    def __call__(self):
        print("제품 가격을 계산합니다.")
        s = 0
        for item in self.price_list:
            s += item
        print("")
        return s
# Client
class Client:
    def __init__(self):
        pass
    def select_items(self, item_list):
        self.item_list = item_list
    def buy(self):
        Store().buy(self.item_list)


if __name__ == "__main__":
    client = Client()
    client.select_items(["pen", "pencel", "keyboard", "computer"])
    client.buy()