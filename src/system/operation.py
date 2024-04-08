from typing import Dict, List


class Operation:
    """Class Operation is a factory for creating operations"""
    # attributes
    __name: str
    __parameters: tuple[str]
    __arguments: Dict[str, str]
    __data: List[any]
    __status: int

    def __init__(self, name, parameters, execute, cancel):
        self.__name = name
        self.__parameters = parameters
        self.__arguments = {}
        self.__data = []
        self.__status = 0
        self.__execute = execute
        self.__cancel = cancel

    def __str__(self):
        s = " ".join([f"{arg}={self.__arguments[arg]}" for arg in self.__arguments.keys()])
        return f"{self.__name} {s}"

    def __int__(self):
        return self.__status

    def __bool__(self):
        return True

    def execute(self):
        self.__status = self.__execute()
        return self

    def cancel(self):
        if self.__status == 1:
            self.__cancel()
        self.__status = -1
        return self

    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters):
        self.__parameters = parameters

    def assign_values(self, **kwargs):
        self.__arguments = kwargs

    @property
    def arguments(self):
        return self.__arguments

    @property
    def data(self):
        return self.__data
