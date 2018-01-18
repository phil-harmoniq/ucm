def say_hello(app_name: str, app_version: str) -> None:
    print("-------------------- ", end="")
    print(f"{app_name} v{app_version}")
    print(" --------------------", end="")


def say_bye() -> None:
    print("--------------------")
