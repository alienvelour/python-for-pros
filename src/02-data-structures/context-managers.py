import time
from contextlib import contextmanager

# Without a context manager
f = open("tasks.txt")
try:
    content = f.read()
finally:
    f.close()

# Using a context manager
with open("tasks.txt") as f:
    content = f.read()


class Section:
    def __init__(self, label: str) -> None:
        self.label = label

    def __enter__(self) -> "Section":
        print(f"--- {self.label} ---")
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        print(f"--- end {self.label} ---")


with Section("normalize tasks"):
    print("doing work")


@contextmanager
def timer(label: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"{label}: {elapsed_ms:.2f}ms")


raw_tasks = [{"title": "  task one  "}, {"title": "task two"}]

with timer("normalize tasks"):
    normalized = [t["title"].strip().title() for t in raw_tasks]
    print(normalized)
