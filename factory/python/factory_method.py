from abc import ABCMeta, abstractmethod


"""
    Senario
    펜/연필 단품을 생산하는 코드
"""
class Writer(metaclass=ABCMeta):
    def __init__(self):
        self.parts_list = [] # 연필이나 펜을 만들기 위한 부품 리스트
    
    @abstractmethod
    def get_parts_list(self):
        return self.parts_list


class Pen(Writer):
    def __init__(self):
        super().__init__()
        self.parts_list.append('ink 10ml')
        self.parts_list.append('aluminum')
        self.parts_list.append('button')
        self.parts_list.append('spring')
    
    def get_parts_list(self):
        print("this is pen's part list")
        return self.parts_list

class Pencel(Writer):
    def __init__(self):
        super().__init__()
        self.parts_list.append('black smoke')
        self.parts_list.append('woods')

    def get_parts_list(self):
        print("this is pen's part list")
        return self.parts_list


# Creator
class WriteCreator(metaclass=ABCMeta):
    def __init__(self):
        self.writer = None
        self.createWriter()
    
    @abstractmethod
    def createWriter(self):
        pass

    def getWriter(self):
        return self.writer

class PenCreator(WriteCreator):
    def __init__(self):
        super().__init__()
    
    def createWriter(self):
        self.writer = Pen()

class PencelCreator(WriteCreator):
    def __init__(self):
        super().__init__()
    
    def createWriter(self):
        self.writer = Pencel()


if __name__ == "__main__":
    # Get Pencel
    pencel_creator = PencelCreator()
    pencel_creator.createWriter()
    print(pencel_creator.getWriter())

    # Get Pen
    pen_creator = PenCreator()
    pen_creator.createWriter()
    print(pen_creator.getWriter())