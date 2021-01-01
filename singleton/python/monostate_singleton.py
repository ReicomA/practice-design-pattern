# state label

class Printer:
    __state = {"is_printing": False}
    def __init__(self):
        self.__dict__ = self.__state
        self.printed_string = []
        self.buffer = None

    def add_string(self, new_string: str):
        self.printed_string.append(new_string)

    def start_printing(self):
        if self.__dict__['is_printing'] == True:
            print("printer is so busy")
        else:
            self.__dict__['is_printing'] = True
            self.buffer = self.printed_string[0]
            del self.printed_string[0]

    
    def end_print(self):
        if self.__dict__['is_printing'] == False:
            print("this printer is not printing")
        else:
            print(self.buffer)
            self.buffer = None
            self.__dict__['is_printing'] = False

if __name__ == "__main__":
    p1 = Printer()
    p2 = Printer()

    # Error
    p2.end_print()
    print("")

    p1.add_string("hello")
    p2.add_string("world")

    p2.start_printing()

    # Error because p1 is aleady printing
    p1.start_printing()
    print("")
    
    p2.end_print()
    p1.start_printing()
    p1.end_print()
    

