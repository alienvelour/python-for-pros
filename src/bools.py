from datetime import date


def is_overdue(due_date: date, status: str) -> bool:
    if due_date is None:
        return False
    if status == "done":
        return False
    return due_date < date.today()


status = "planned"

if status == "done":
    print("The project is done.")
elif status == "blocked":
    print("The project is blocked.")
else:
    print("The project is in progress.")
