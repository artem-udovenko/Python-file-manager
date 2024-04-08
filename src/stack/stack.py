from src.stack.node import Node


class Stack:
    """Operation call stack"""
    # static
    single = 0
    __stack = None
    # attributes
    __top: int
    __list: list[Node]

    def __init__(self):
        assert Stack.single == 0, f"{Colors.RED}Too many stacks{Colors.ENDC}"
        self.__top = 0
        self.__list = [Node(None)]
        Stack.single = 1
        Stack.__stack = self

    @staticmethod
    def stack():
        return Stack.__stack

    @property
    def top(self):
        return self.__list[self.__top].operation

    def push(self, operation):
        if operation is None:
            return self
        node = Node(operation)
        if self.__top != len(self.__list) - 1:
            self.__list = self.__list[:self.__top + 1]
        self.__list.append(node)
        self.__top += 1
        return self

    def pop(self):
        if self.__list[self.__top].operation is None:
            return self
        self.__top -= 1
        return self

    def can_undo(self):
        return self.__top != 0

    def can_redo(self):
        return self.__top != len(self.__list) - 1

    def rollback(self):
        if self.can_redo():
            self.__top += 1
        return self

