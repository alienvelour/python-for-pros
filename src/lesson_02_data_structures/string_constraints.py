from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints

# StringConstraints(strip_whitespace=True, min_length=2, max_length=120)
StrippedName = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=2, max_length=120)
]


class TaskCreate(BaseModel):
    name: StrippedName


class ProjectCreate(BaseModel):
    name: StrippedName
    description: str | None = Field(default=None, max_length=1000)
