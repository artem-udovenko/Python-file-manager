from src.system.operation import Operation


class Node:
    """Supporting structure for the stack"""
    # attributes
    __operation: Operation

    def __init__(self, operation: Operation):
        self.__operation = operation

    @property
    def operation(self):
        return self.__operation

