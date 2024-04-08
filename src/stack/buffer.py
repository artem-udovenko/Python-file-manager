import shutil
from docs.system_features import separator


class Buffer:
    """Buffer is a singleton that stores a temporary reference to file"""
    # static
    single = 0
    __buffer = None
    # attributes
    __path: str

    def __init__(self):
        assert Buffer.single == 0, f"{Colors.RED}Too many buffers{Colors.ENDC}"
        self.__path = ""
        Buffer.single = 1
        Buffer.__buffer = self

    @staticmethod
    def buffer():
        return Buffer.__buffer

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    def place(self, directory: str):
        if self.path:
            shutil.copyfile(self.path, directory + separator + self.path.split(separator)[-1])
        return self

