import os
from abc import abstractmethod, ABCMeta

# 작성 내용

# Receiver
class EditEngine:
    
    def __init__(self):
        self.string_list = []

    def write(self, text):
        self.string_list.append(text)
        return True

    def back(self):
        if len(self.string_list) >= 1:
            self.string_list.pop()
            return True
        else:
            return False

    def print_text(self):
        result = ""
        for data in self.string_list:
            result += data
        print(result)


# Command
class EditCommand(metaclass=ABCMeta):
    
    def __init__(self, edit_engine):
        self.edit_engine = edit_engine
    def execute(self):
        pass

class WriteCommand(EditCommand):
    def __init__(self, edit_engine, text):
        super().__init__(edit_engine)
        self.text = text
    def execute(self):
        self.edit_engine.write(self.text)

class BackCommand(EditCommand):
    def __init__(self, edit_engine):
        super().__init__(edit_engine)
    def execute(self):
        self.edit_engine.back()

class PrintCommand(EditCommand):
    def __init__(self, edit_engine):
        super().__init__(edit_engine)
    def execute(self):
        self.edit_engine.print_text()


# Invoke
class Editor:
    def __init__(self):
        self.__command_queue = []
    
    def place_order(self, command):
        self.__command_queue.append(command)

    def run(self):
        for command in self.__command_queue:
            command.execute()
        


if __name__ == "__main__":
    edit_engine = EditEngine()

    """Command
    write: hello
    write: python
    back:
    write: world
    print_text:

    RESULT: helloworld
    """

    editor = Editor()
    editor.place_order(WriteCommand(edit_engine, "hello"))
    editor.place_order(WriteCommand(edit_engine, " "))
    editor.place_order(WriteCommand(edit_engine, "python"))
    editor.place_order(BackCommand(edit_engine))
    editor.place_order(WriteCommand(edit_engine, "world"))
    editor.place_order(PrintCommand(edit_engine))

    editor.run()