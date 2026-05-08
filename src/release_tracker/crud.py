from datetime import UTC, datetime

from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from .models import (
    Project,
    ProjectCreate,
    ProjectUpdate,
    Task,
    TaskCreate,
    TaskPriority,
    TaskStatus,
    TaskUpdate,
)


def slugify(value: str) -> str:
    cleaned = "".join(c for c in value.lower() if c.isalnum() or c == " ")
    return "-".join(cleaned.split()) or "project"


def list_projects(session: Session) -> list[Project]:
    statement = select(Project).order_by(Project.name)
    return list(session.exec(statement).all())


def get_project(session: Session, project_id: int) -> Project | None:
    return session.get(Project, project_id)


def create_project(session: Session, payload: ProjectCreate) -> Project:
    project = Project.model_validate(
        payload, update={"slug": slugify(payload.name)}
    )
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def update_project(
    session: Session, project: Project, payload: ProjectUpdate
) -> Project:
    updated_fields = payload.model_dump(exclude_unset=True)
    project.sqlmodel_update(updated_fields)

    if "name" in updated_fields and updated_fields["name"] is not None:
        project.slug = slugify(updated_fields["name"])

    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def delete_project(session: Session, project: Project) -> None:
    session.delete(project)
    session.commit()


def list_tasks(
    session: Session,
    *,
    project_id: int | None = None,
    project_slug: str | None = None,
    task_status: TaskStatus | None = None,
    task_priority: TaskPriority | None = None,
    overdue_only: bool = False,
) -> list[Task]:
    statement = select(Task).options(selectinload(Task.project))  # type: ignore[arg-type]

    # TODO: Apply each filter to `statement` only when its argument was passed.
    #
    # - project_id: where Task.project_id == project_id
    # - project_slug: join Project, where Project.slug == project_slug
    # - task_status: where Task.status == task_status
    # - task_priority: where Task.priority == task_priority
    # - overdue_only: where Task.due_date is not None, Task.due_date < today,
    #   Task.status != TaskStatus.done
    #
    # Use `today = datetime.now(UTC).date()` for the overdue comparison.

    return list(session.exec(statement).all())


def get_task(session: Session, task_id: int) -> Task | None:
    statement = (
        select(Task)
        .options(selectinload(Task.project))  # type: ignore[arg-type]
        .where(Task.id == task_id)
    )
    return session.exec(statement).first()


def create_task(
    session: Session, project_id: int, payload: TaskCreate
) -> Task:
    task = Task.model_validate(payload, update={"project_id": project_id})
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def update_task(session: Session, task: Task, payload: TaskUpdate) -> Task:
    task.sqlmodel_update(payload.model_dump(exclude_unset=True))
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def delete_task(session: Session, task: Task) -> None:
    session.delete(task)
    session.commit()
