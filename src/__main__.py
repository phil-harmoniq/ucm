import sys
from typing import List
import printer

APP_NAME = "Unix Config Manager"
APP_VERSION = "0.0.1"


def main():
    printer.say_hello(APP_NAME, APP_VERSION)
    cli_args = sys.argv
    print(cli_args[0])


def parse_args(args: List[str]) -> None:
    print(args)
