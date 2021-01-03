from abc import ABCMeta, abstractmethod


"""
    Senario
    펜/연필이 여러개 있는 세트 2가지를 생성하는 코드
    Set1: Pen 2개, 연필 5개
    Set2: Pen 5개, 연필 7개
"""

# 펜과 연필들
class Writer(metaclass=ABCMeta):
    def __init__(self):
        self.parts_list = [] # 연필이나 펜을 만들기 위한 부품 리스트
    
    @abstractmethod
    def get_parts_list(self):
        return self.parts_list
    
    @abstractmethod
    def get_name(self):
        pass


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

    def get_name(self):
        return "pen"

class Pencel(Writer):
    def __init__(self):
        super().__init__()
        self.parts_list.append('black smoke')
        self.parts_list.append('woods')

    def get_parts_list(self):
        print("this is pen's part list")
        return self.parts_list
    
    def get_name(self):
        return "pencel"

# 세트들
class SetFactory(metaclass=ABCMeta):
    
    @abstractmethod
    def createPens(self):
        pass
    
    @abstractmethod
    def createPencels(self):
        pass

class Set1Factory(SetFactory):

    def createPens(self):
        return [Pen()] * 2
    def createPencels(self):
        return [Pencel()] * 5

class Set2Factory(SetFactory):
    def createPens(self):
        return [Pen()] * 5
    def createPencels(self):
        return [Pencel()] * 7

if __name__ == "__main__":
    
    for factory in [Set1Factory(), Set2Factory()]:
        factory = factory
        pens = factory.createPens()
        pencels = factory.createPencels()
        print(factory)
        for pen in pens:
            print(pen.get_name())
        for pencel in pencels:
            print(pencel.get_name())
        print("")

    