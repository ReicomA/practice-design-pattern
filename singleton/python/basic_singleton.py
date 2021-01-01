class Printer(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Printer, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.printed_data = []
    
    def add_string(self, new_string: str):
        self.printed_data.append(new_string)
    
    def print(self) -> bool:
        if len(self.printed_data) == 0:
            return False
        else:
            target_data = self.printed_data[0]
            del self.printed_data[0]
            print(target_data)
            return True


if __name__ == "__main__":
    printer1 = Printer()
    printer2 = Printer()

    printer1.add_string("hello")
    printer2.add_string("world")

    printer2.print()
    printer1.print()