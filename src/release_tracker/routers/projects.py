from typing import Any

from fastapi import APIRouter, Response, status

from release_tracker import crud
from release_tracker.dependencies import ProjectDep, SessionDep
from release_tracker.models import ProjectCreate, ProjectRead, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=list[ProjectRead])
def list_projects(session: SessionDep) -> Any:
    # TODO: Call `crud.list_projects` with the session and return the result.
    pass


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project: ProjectDep) -> Any:
    # TODO: `ProjectDep` already fetched the project (and raised 404 if missing). Return it.
    pass


@router.post(
    "/", response_model=ProjectRead, status_code=status.HTTP_201_CREATED
)
def create_project(payload: ProjectCreate, session: SessionDep) -> Any:
    # TODO: Call `crud.create_project` with the session and payload, and return the result.
    pass


@router.patch("/{project_id}", response_model=ProjectRead)
def update_project(
    project: ProjectDep, payload: ProjectUpdate, session: SessionDep
) -> Any:
    # TODO: Call `crud.update_project` with the session, the existing project, and the payload. Return the updated project.
    pass


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project: ProjectDep, session: SessionDep) -> Response:
    # TODO: Call `crud.delete_project` with the session and the project, then return a `Response` with `status_code=status.HTTP_204_NO_CONTENT`.
    pass
