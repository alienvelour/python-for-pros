def slug(name: str) -> str:
    return name.lower().replace(" ", "-")


def add(a: int, b: int) -> int:
    return a + b


print(add("Hello", "Nina"))  # This works generally, mypy will complain


def greet(name: str) -> None:
    print(f"Hello, {name}!")


project_name: str = "release tracker"

counts: dict[str, int] = {}

name: str | None = "Nina"
