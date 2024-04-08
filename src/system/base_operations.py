import os
import inspect
import sys
from src.admin.admin import Admin
from src.system.operation import Operation
from docs.colors import Colors
from docs.system_features import separator


"""base_operations.py includes cancellable operations that can be added to call stack"""


def get(name: str):
    for cl in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        if cl[0] == name and cl[0] not in ("Admin", "Operation", "Colors"):
            return eval(f"{name}()")


class cd(Operation):
    def __init__(self):
        super().__init__("cd", ("destination", ), self.change_directory, self.change_directory_)

    def change_directory(self):
        destination = super().arguments["destination"]
        super().data.append(Admin.admin().wd)
        if destination == "..":
            tmp = Admin.admin().wd.split(separator)
            if len(tmp) > 1:
                tmp.pop()
            Admin.admin().wd = separator.join(tmp)
            return 1
        for directory in next(os.walk(Admin.admin().wd))[1]:
            if destination == directory:
                Admin.admin().wd = f"{Admin.admin().wd}\\{directory}"
                return 1
        print(f"{Colors.RED}fatal: no such directory{Colors.ENDC}")
        return -1

    def change_directory_(self):
        Admin.admin().wd = super().data[-1]
        super().data.pop()
        return


class copy(Operation):
    def __init__(self):
        super().__init__("copy", ("file", ), self.copy_file, self.copy_file_)

    def copy_file(self):
        if separator in self.arguments["file"]:
            if not os.path.exists(self.arguments["file"]):
                print(f"{Colors.RED}fatal: no such file{Colors.ENDC}")
                return -1
            super().data.append(Admin.buffer().path)
            Admin.buffer().path = super().arguments["file"]
            return 1
        if not self.arguments["file"] in next(os.walk(Admin.admin().wd))[2]:
            print(f"{Colors.RED}fatal: no such file{Colors.ENDC}")
            return -1
        super().data.append(Admin.buffer().path)
        Admin.buffer().path = Admin.admin().wd + separator + super().arguments["file"]
        return 1

    def copy_file_(self):
        Admin.buffer().path = super().data[-1]
        super().data.pop()
        return


class paste(Operation):
    def __init__(self):
        super().__init__("paste", (), self.paste_file, self.paste_file_)

    def paste_file(self):
        if not os.path.exists(Admin.buffer().path):
            print(f"{Colors.RED}fatal: the file no more exists{Colors.ENDC}")
            return -1
        self.data.append(Admin.admin().wd + separator + Admin.buffer().path.split(separator)[-1])
        Admin.buffer().place(Admin.admin().wd)
        return 1

    def paste_file_(self):
        if os.path.exists(self.data[-1]):
            os.remove(self.data[-1])
        return



