from app import ma
from models import Task


class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = True


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
