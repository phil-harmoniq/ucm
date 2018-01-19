from printer import say_bye


def exit_app(exit_code: int = 1) -> None:
    say_bye()
    exit(exit_code)
