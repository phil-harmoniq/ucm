import sys
from typing import List
import printer
from app_info import APP_NAME, APP_VERSION
import installer


def main(app_name: str, app_version: str, args: List[str]) -> None:
    printer.say_hello(app_name, app_version)
    cli_args = args
    parse_args(cli_args)


def parse_args(args: List[str]) -> None:
    if args[1] == "install":
        installer.add_ucm_symlink()
    else:
        raise ValueError()


main(APP_NAME, APP_VERSION, sys.argv)
