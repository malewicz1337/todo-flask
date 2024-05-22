from flask import Blueprint, jsonify, request

from ..extensions import db
from .models import Task
from .schemas import task_schema, tasks_schema

task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@task_bp.route("/test", methods=["GET"])
def test():
    return "<p>Hello, World!</p>"


@task_bp.route("/", methods=["POST"])
def add_task():
    title = request.json.get("title")
    description = request.json.get("description")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)


@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return tasks_schema.jsonify(tasks)


@task_bp.route("/<int:id>", methods=["GET"])
def get_task(id):
    task = Task.query.get_or_404(id)
    return task_schema.jsonify(task)


@task_bp.route("/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)
    title = request.json.get("title")
    description = request.json.get("description")

    if title:
        task.title = title
    if description:
        task.description = description

    db.session.commit()
    return task_schema.jsonify(task)


@task_bp.route("/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"})
