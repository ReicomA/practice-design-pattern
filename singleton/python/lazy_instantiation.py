class Printer:
    __instance = None
    

    def __init__(self):
        if not Printer.__instance: #존재하지 않는 경우
            self.printed_string = []
        else: # 존재하는 경우
            print("Aleady inited")

    def add_string(self, new_string: str) -> bool:
        if isinstance(self.printed_string, list):
            self.printed_string.append(new_string)
            return True
        else:
            print("instance not inited")
            return False

    def print(self):
        if isinstance(self.printed_string, list):
            if len(self.printed_string) == 0:
                print("noting to print")
            else:
                target_string = self.printed_string[0]
                del self.printed_string[0]
                print(target_string)
        else:
            print("instance not inited")

    @classmethod
    def get_instance(cls) -> bool:
        if not cls.__instance:
            cls.__instance = Printer()
        return cls.__instance

if __name__ == "__main__":
    p0 = Printer()
    p0.print() #Error
    print("")

    p1 = Printer.get_instance()
    p2 = Printer.get_instance()

    p1.add_string("hello")
    p2.add_string("world")

    p1.print()
    p2.print()