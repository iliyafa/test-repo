import sys
from pathlib import Path


def greet(name: str) -> str:
    return f"Hello, {name}!"


def find_python_files(directory: str) -> list[Path]:
    root = Path(directory)
    if not root.is_dir():
        print(f"Error: {directory} is not a valid directory", file=sys.stderr)
        return []
    return sorted(root.rglob("*.py"))


def main():
    print(greet("world"))

    files = find_python_files(".")
    print(f"Found {len(files)} Python file(s):")
    for f in files:
        print(f"  {f}")


if __name__ == "__main__":
    main()
