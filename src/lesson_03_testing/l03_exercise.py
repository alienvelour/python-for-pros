from datetime import date
from enum import StrEnum


class TaskStatus(StrEnum):
    planned = "planned"
    in_progress = "in_progress"
    blocked = "blocked"
    done = "done"


def is_overdue(due_date: date | None, status: str) -> bool:
    if not due_date:
        return False
    return due_date < date.today() and status != TaskStatus.done


def next_status(current: TaskStatus) -> TaskStatus:
    match current:
        case TaskStatus.planned:
            return TaskStatus.in_progress
        case TaskStatus.in_progress:
            return TaskStatus.done
        case TaskStatus.done | TaskStatus.blocked:
            return current
