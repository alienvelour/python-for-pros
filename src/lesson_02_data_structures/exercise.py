from dataclasses import dataclass

project_names = ["Payments API", "Developer Portal", "Ops Console"]

slugs = []
for name in project_names:
    slugs.append(name.lower().replace(" ", "-"))
print(slugs)

slugs = [name.lower().replace(" ", "-") for name in project_names]
print(slugs)

tasks = [
    {"title": "ship docs", "done": False},
    {"title": "cut release", "done": True},
    {"title": "announce launch", "done": False},
]

open_titles = []
for task in tasks:
    if not task["done"]:
        open_titles.append(task["title"])
print(open_titles)

open_titles = [task["title"] for task in tasks if not task["done"]]
print(open_titles)


def validate_project_name(name):
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("Project name cannot be empty")
    return cleaned


print(validate_project_name("My Project"))

try:
    name = validate_project_name("   ")
except ValueError as e:
    print(f"Error: {e}")
    name = "DEFAULT"

print(f"Final project name: {name}")


@dataclass
class Project:
    name: str
    slug: str
    archived: bool = False


project = Project(name="My Project", slug="my-project")
print(project)
