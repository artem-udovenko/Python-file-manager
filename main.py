from src.admin.admin import Admin
from docs.colors import Colors
from re import fullmatch


def main():
    admin = Admin()
    print(f"""
{Colors.YELLOW}{Colors.UNDERLINE}Welcome to Python File Manager.This program will help you to manage your files.
Type 'exit' to exit the program. Type 'help' for more information.{Colors.ENDC}{Colors.ENDC}
""")
    commands = []
    while True:
        command = input(f"{Colors.GREEN}{Admin.admin().wd} -> {Colors.ENDC}")
        if fullmatch(r"\^+", command):
            try:
                command = commands[-len(command)]
            except IndexError:
                pass
            finally:
                print(f"{Colors.YELLOW}Command used: {command}{Colors.ENDC}")
        match command:
            case "":
                continue
            case "exit":
                print(f"\n{Colors.YELLOW}Thank you for using Python File Manager! Exiting program...{Colors.ENDC}\n")
                break
            case "help":
                with open("docs/help.txt", "r") as file:
                    print(f"{Colors.BOLD}{file.read()}{Colors.ENDC}")
                    commands.append(command)
                continue
        Admin.admin().process(command.split())
        commands.append(command)


if __name__ == "__main__":
    main()
