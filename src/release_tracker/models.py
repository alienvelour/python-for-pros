from datetime import UTC, date, datetime
from enum import StrEnum
from typing import Annotated

from pydantic import StringConstraints
from sqlalchemy import Column, DateTime
from sqlmodel import Field, Relationship, SQLModel


def utc_now() -> datetime:
    return datetime.now(UTC)


class TaskStatus(StrEnum):
    planned = "planned"
    in_progress = "in_progress"
    blocked = "blocked"
    done = "done"


class TaskPriority(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"


ProjectName = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=2),
]

TaskTitle = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=2),
]


# --- Project ---


class ProjectBase(SQLModel):
    name: ProjectName = Field(unique=True)
    description: str | None = None


class Project(ProjectBase, table=True):
    __tablename__ = "projects"

    id: int | None = Field(default=None, primary_key=True)
    slug: str = Field(unique=True)

    tasks: list["Task"] = Relationship(back_populates="project")

    created_at: datetime = Field(
        default_factory=utc_now,
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(SQLModel):
    name: ProjectName | None = None
    description: str | None = None


class ProjectRead(ProjectBase):
    id: int
    slug: str
    created_at: datetime


# --- Task ---


class TaskBase(SQLModel):
    # TODO: Define the shared fields for a task.
    #
    # A task has a title, optional free-text details, a status, a priority,
    # and an optional due date.
    #
    # Use TaskTitle for the title (same idea as ProjectName above).
    # Use the TaskStatus and TaskPriority enums for status and priority.
    # Pick sensible defaults: a new task starts as "planned" with "medium"
    # priority.
    #
    # Look at ProjectBase for how required fields, optional fields, and
    # fields with defaults are declared.
    pass


class Task(TaskBase, table=True):
    __tablename__ = "tasks"

    id: int | None = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="projects.id", index=True)

    project: Project = Relationship(back_populates="tasks")


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    # TODO: The update schema for PATCH requests.
    #
    # PATCH semantics: a client sends only the fields it wants to change.
    # Fields not included in the request body stay untouched.
    #
    # What does that imply about defaults here?
    # Compare with ProjectUpdate above.
    pass


class TaskRead(TaskBase):
    # TODO: The read schema adds server-generated fields that don't exist
    # at creation time but should appear in API responses.
    #
    # Which fields does the Task table model have that TaskBase doesn't?
    # Compare with ProjectRead above.
    pass
