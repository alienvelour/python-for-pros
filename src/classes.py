from dataclasses import dataclass


@dataclass
class Project:
    name: str
    slug: str
    archived: bool = False

    def archive(self) -> None:
        self.archived = True


project = Project(name="Payments API", slug="payments-api")
project2 = Project(name="Payments API", slug="payments-api")
print(project)
print(project.slug)
print(project == project2)
project.archive()
print(project.archived)
print(project == project2)
