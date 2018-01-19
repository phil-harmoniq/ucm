import sys
from typing import List
import printer
import installer


def main(args: List[str]) -> None:
    printer.say_hello()
    parse_args(args)
    printer.say_bye()


def parse_args(args: List[str]) -> None:
    if len(args) > 1:
        if args[1] == "install":
            installer.install_launch_script()
        elif args[1] == "remove":
            installer.remove_launch_script()
        else:
            raise ValueError()
    else:
        return


main(sys.argv)
