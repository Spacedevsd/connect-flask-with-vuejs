from .app import ma

class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "name",)

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)