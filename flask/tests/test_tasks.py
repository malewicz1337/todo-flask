import json

from models import Task


def test_add_task(test_client):
    response = test_client.post(
        "/tasks/",
        data=json.dumps({"title": "Test Task", "description": "Test Description"}),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"


def test_get_tasks(test_client):
    response = test_client.get("/tasks/")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_task(test_client):
    task = Task.query.first()
    response = test_client.get(f"/tasks/{task.id}")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["title"] == task.title
    assert data["description"] == task.description


def test_update_task(test_client):
    task = Task.query.first()
    response = test_client.put(
        f"/tasks/{task.id}",
        data=json.dumps({"title": "Updated Task"}),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["title"] == "Updated Task"
    assert data["description"] == task.description


def test_delete_task(test_client):
    task = Task.query.first()
    response = test_client.delete(f"/tasks/{task.id}")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert data["message"] == "Task deleted successfully"
    assert Task.query.get(task.id) is None
