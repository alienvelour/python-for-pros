from fastapi.testclient import TestClient


def test_create_task(client: TestClient, sample_project_id: int):
    response = client.post(
        f"/projects/{sample_project_id}/tasks",
        json={
            "title": "Add settings page",
            "priority": "high",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Add settings page"
    assert data["status"] == "planned"
    assert data["priority"] == "high"
    assert data["project_id"] == sample_project_id
    assert data["project_name"] == "Release Platform"
    assert data["project_slug"] == "release-platform"


def test_get_task(client: TestClient, sample_task_id: int):
    response = client.get(f"/tasks/{sample_task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == sample_task_id


def test_get_task_not_found(client: TestClient):
    response = client.get("/tasks/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_list_tasks_filter_by_status(
    client: TestClient, sample_project_id: int
):
    # TODO: Create two tasks (one with status="planned", one with status="done"),
    # then GET /tasks?status=done and assert that only the done task comes back.
    pass


def test_list_tasks_filter_by_project_slug(
    client: TestClient, sample_project_id: int
):
    # TODO: Create a second project, post one task to each project, then
    # GET /tasks?project_slug=<second-project-slug> and assert that only
    # the second project's task comes back.
    pass
