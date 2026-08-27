def slugify(name: str, sep: str = "-") -> str:
    cleaned = name.strip().lower()
    return cleaned.replace(" ", sep)


print(slugify("Payment API"))
print(slugify("Payment API", sep="*"))


def add_tag(name: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []
    tags.append(name)
    return tags


tags: list[str] = []
add_tag("foo", tags)
add_tag("bar", tags)
tags = add_tag("baz", tags)
print(tags)


def archive_project(name, *, notify=False, force=False):
    if force:
        print(f"Force archive {name}")
    if notify:
        print(f"sent notification for {name}")


archive_project("payments-api", notify=True)
archive_project("payments-api", notify=True, force=True)


def build_project(name, **kwargs):
    project = {"name": name, "slug": slugify(name)}
    project.update(kwargs)
    return project


project = build_project(
    "payments-api", description="Does checkout", archive=False
)
print(project)
