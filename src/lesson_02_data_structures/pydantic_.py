from pydantic import BaseModel, Field, ValidationError


class ProjectCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    description: str | None = Field(default=None, max_length=1000)


if __name__ == "__main__":
    project = ProjectCreate(name="Release Tracker")
    print(project)

    try:
        project = ProjectCreate(
            name="R", description="Let's track some releases"
        )
        print(project)
    except ValidationError as e:
        print(f"ValidationError: {e}")
