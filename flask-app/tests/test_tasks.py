import json

from app.tasks.models import Task


def test_add_task(client, session):
    response = client.post(
        "/tasks/", json={"title": "Test Task", "description": "This is a test task"}
    )
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"


def test_get_tasks(client, session):
    task1 = Task(title="Task 1", description="First task")
    task2 = Task(title="Task 2", description="Second task")
    session.add(task1)
    session.add(task2)
    session.commit()

    response = client.get("/tasks/")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert len(data) == 2


def test_get_task(client, session):
    task = Task(title="Test Task", description="This is a test task")
    session.add(task)
    session.commit()

    response = client.get(f"/tasks/{task.id}")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["title"] == "Test Task"
    assert data["description"] == "This is a test task"


def test_update_task(client, session):
    task = Task(title="Old Task", description="Old description")
    session.add(task)
    session.commit()

    response = client.put(
        f"/tasks/{task.id}",
        json={"title": "New Task", "description": "New description"},
    )
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["title"] == "New Task"
    assert data["description"] == "New description"


def test_delete_task(client, session):
    task = Task(title="Task to be deleted", description="This task will be deleted")
    session.add(task)
    session.commit()

    response = client.delete(f"/tasks/{task.id}")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["message"] == "Task deleted successfully"
    assert session.query(Task).filter_by(id=task.id).first() is None
