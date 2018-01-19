import sys
from typing import List
from app_helper import exit_app
import printer
import installer


def main(args: List[str]) -> None:
    if not args:
        printer.show_help_menu()
        exit(0)
    if exclusive_args(args):
        exit(0)
    printer.say_hello()
    parse_args(args)
    exit_app(0)


def parse_args(args: List[str]) -> None:
    if args[0] == "install":
        installer.install_launch_script()
    elif args[0] == "remove":
        installer.remove_launch_script()
    else:
        print(f"Invalid command: {args[0]}")
        exit_app(1)


def exclusive_args(args: List[str]) -> bool:
    for arg in args:
        if arg == "-h" or arg == "--help":
            printer.show_help_menu()
            return True
        elif arg == "--version":
            printer.show_version()
            return True
    return False


main(sys.argv[1:])
