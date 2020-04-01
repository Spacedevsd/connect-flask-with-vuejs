from flask import Blueprint, render_template, jsonify, request
from time import sleep

from app.models import Task
from app.app import db
from app.schemas import tasks_schema, task_schema

tasks = Blueprint("tasks", __name__, url_prefix="/tasks")


@tasks.route("/")
def task_html():
    return render_template("tasks.html")


@tasks.route("/list")
def get_tasks():
    tasks = tasks_schema.dump(Task.query.all())
    return jsonify(tasks)


@tasks.route("/insert", methods=["POST"])
def insert_task():
    # pegando os dados que vem do VueJS
    data = request.get_json()

    # criei um objeto task a partir dos dados do front-end
    task = Task()
    task.name = data["name"]
    
    # salvei os dados no banco
    db.session.add(task)
    db.session.commit()

    # Serialzamos o dados
    task_serialized = task_schema.dump(task)

    # Aguarda 5 segundos antes de enviar os dados para o front
    sleep(5)

    # Enviamos os dados para o frontend
    return jsonify(task_serialized)
