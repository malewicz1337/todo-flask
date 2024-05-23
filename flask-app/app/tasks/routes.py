from flask import Blueprint, jsonify, request

from app.extensions import db
from app.tasks.models import Task
from app.tasks.schemas import task_schema, tasks_schema


task_bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@task_bp.route("/", methods=["POST"])
def add_task():
    title = request.json.get("title")
    description = request.json.get("description")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    new_task = Task(title=title, description=description)

    try:
        db.session.add(new_task)
        db.session.commit()
        return task_schema.jsonify(new_task), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return tasks_schema.jsonify(tasks)


@task_bp.route("/<int:id>", methods=["GET"])
def get_task(id):
    task = db.session.get(Task, id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return task_schema.jsonify(task)


@task_bp.route("/<int:id>", methods=["PUT"])
def update_task(id):
    task = db.session.get(Task, id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    title = request.json.get("title")
    description = request.json.get("description")

    if title:
        task.title = title
    if description:
        task.description = description

    try:
        db.session.commit()
        return task_schema.jsonify(task)
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@task_bp.route("/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = db.session.get(Task, id)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({"message": "Task deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
