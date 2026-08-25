from enum import StrEnum, auto


class TaskStatus(StrEnum):
    planned = auto()
    in_progress = auto()
    blocked = auto()
    done = auto()


status = TaskStatus.in_progress
print(status)
