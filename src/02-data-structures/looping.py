fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)

person = {"name": "Alice", "age": 30, "city": "New York"}

for key, value in person.items():
    print(f"{key}: {value}")

project_names = [
    "Payments API",
    "Orders API",
    "Portal",
    "User Management API",
    "Inventory API",
]

slugs = [name.lower().replace(" ", "-") for name in project_names]
print(slugs)

tasks = [
    {"title": "Implement Payments API", "completed": True},
    {"title": "Implement Orders API", "completed": False},
    {"title": "Implement Portal", "completed": True},
    {"title": "Implement User Management API", "completed": False},
    {"title": "Implement Inventory API", "completed": False},
]

open_tasks = [task["title"] for task in tasks if not task["completed"]]
print(open_tasks)

single_task = {"title": "Implement Payments API", "completed": True}
print(single_task.get("title", "No title"))

num_open_tasks = sum(
    1 for task in tasks if not task["completed"]
)  # generator expression
print(num_open_tasks)

for name, slug in zip(project_names, slugs):
    print(f"{name} -> {slug}")
