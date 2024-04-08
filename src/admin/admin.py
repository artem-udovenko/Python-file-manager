import os
from datetime import datetime
from docs.colors import Colors
from src.stack.buffer import Buffer
from src.stack.stack import Stack
from docs.system_features import separator


def dfs_tree(path, depth=0):
    root, dirs, files = next(os.walk(path))
    root = root.split(separator)[-1]
    print("\t" * depth + f"{Colors.BLUE}{root}{separator}{Colors.ENDC}")
    for file in files:
        print("\t" * (depth + 1) + file)
    for directory in dirs:
        dfs_tree(separator.join([path, directory]), depth + 1)


def validation(path: str, msg: any):
    if separator in path:
        if not os.path.exists(path):
            print(f"{Colors.RED}fatal: no such file{Colors.ENDC}")
            return None
        if msg:
            if input(f"Do you want to {msg} {path}? [y/n] ") == "n":
                return None
        return path
    if path not in next(os.walk(Admin.admin().wd))[2]:
        print(f"{Colors.RED}fatal: no such file{Colors.ENDC}")
        return None
    if msg:
        if input(f"Do you want to {msg} {Admin.admin().wd + separator + path}? [y/n] ") == "n":
            return None
    return Admin.admin().wd + separator + path


class Admin:
    """Admin manages operations"""
    # static
    single = 0
    __admin = None
    __buffer: Buffer = None
    __stack: Stack = None
    # attributes
    __wd: str

    def __init__(self):
        assert Admin.single == 0, f"{Colors.RED}Too many admins{Colors.ENDC}"
        Admin.__buffer = Buffer()
        Admin.__stack = Stack()
        Admin.single = 1
        Admin.__admin = self
        self.__wd = os.getcwd()

    @staticmethod
    def admin():
        return Admin.__admin

    @staticmethod
    def buffer():
        return Admin.__buffer

    @staticmethod
    def stack():
        return Admin.__stack

    @property
    def wd(self):
        return self.__wd

    @wd.setter
    def wd(self, wd):
        self.__wd = wd

    def prepare(self, command, operation):
        args = r", ".join([str(operation.parameters[i]) + "=\"" + command[i + 1] + "\"" for i in
                           range(len(operation.parameters))])
        args = args.replace("\\", "/")
        eval(r"operation.assign_values(" + args + r")")
        for arg in operation.arguments.keys():
            operation.arguments[arg] = operation.arguments[arg].replace("/", "\\")
        operation.execute()
        Admin.stack().push(operation)
        return self

    def process(self, command: list):
        match command[0]:
            # There are non-cancellable commands except cd (it can create several operations)
            case "cd":
                from src.system.base_operations import get
                for directory in command[1].split(separator):
                    operation = get("cd")
                    self.prepare([command[0], directory], operation)
                return self
            case "undo":
                if not Admin.stack().can_undo():
                    print(f"{Colors.YELLOW}Nothing to undo{Colors.ENDC}")
                    return self
                if input(f"{Colors.YELLOW}Do you want to undo {str(Admin.stack().top)}? [y/n] {Colors.ENDC}") == "n":
                    return self
                Admin.stack().top.cancel()
                Admin.stack().pop()
                return self
            case "redo":
                if not Admin.stack().can_redo():
                    print(f"{Colors.YELLOW}Nothing to redo{Colors.ENDC}")
                    return self
                Admin.stack().rollback()
                Admin.stack().top.execute()
                return self
            case "buf-show":
                if Admin.buffer().path:
                    print(f"{Colors.BOLD}{Admin.buffer().path}{Colors.ENDC}")
                else:
                    print(f"{Colors.YELLOW}Buffer is empty{Colors.ENDC}")
                return self
            case "graph":
                dfs_tree(self.wd)
                return self
            case "delete":
                path = validation(command[1], "delete")
                if path:
                    os.remove(path)
                return self
            case "exec":
                path = validation(command[1], "execute")
                if path:
                    os.startfile(path)
                return self
            case "rename":
                path = validation(command[1], "rename")
                if path:
                    os.rename(path, Admin.admin().wd + separator + command[2])
                return self
            case "prop":
                path = validation(command[1], None)
                if path:
                    print(f"{Colors.BOLD}Location: {path}{Colors.ENDC}")
                    print(f"{Colors.BOLD}Size: {os.path.getsize(path)} bytes{Colors.ENDC}")
                    print(f"{Colors.BOLD}Created: {datetime.fromtimestamp(os.path.getctime(path))}{Colors.ENDC}")
                return self
        from src.system.base_operations import get
        operation = get(command[0])
        if not operation:
            print(f"{Colors.RED}No such command{Colors.ENDC}")
            return self
        self.prepare(command, operation)
        return self
