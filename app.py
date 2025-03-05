from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Инициализация списка задач
tasks = [
    {"id": 1, "title": "Learn Flask", "description": "Study Flask framework"},
    {"id": 2, "title": "Build a REST API", "description": "Create a simple REST API"}
]

# Вспомогательная функция для поиска задачи по ID
def find_task(task_id):
    """
    Ищет задачу по её ID в списке задач.
    Возвращает задачу, если она найдена, иначе None.
    """
    return next((task for task in tasks if task["id"] == task_id), None)

# Ручка для получения списка всех задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Возвращает список всех задач.
    """
    return jsonify(tasks), 200

# Ручка для получения задачи по ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """
    Возвращает задачу по её ID.
    Если задача не найдена, возвращает ошибку 404.
    """
    task = find_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task), 200

# Ручка для создания новой задачи
@app.route('/tasks', methods=['POST'])
def create_task():
    """
    Создает новую задачу.
    Тело запроса должно содержать 'title' и 'description'.
    Возвращает созданную задачу и статус 201.
    """
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "Invalid request: 'title' is required"}), 400

    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,  # Автоматическое присвоение ID
        "title": request.json["title"],
        "description": request.json.get("description", "")
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Ручка для обновления задачи по ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """
    Обновляет задачу по её ID.
    Тело запроса может содержать 'title' и/или 'description'.
    Возвращает обновленную задачу.
    """
    task = find_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    if not request.json:
        return jsonify({"error": "Invalid request: JSON body is required"}), 400

    task["title"] = request.json.get("title", task["title"])
    task["description"] = request.json.get("description", task["description"])
    return jsonify(task), 200

# Ручка для удаления задачи по ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Удаляет задачу по её ID.
    Возвращает статус успешного выполнения.
    """
    task = find_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    return jsonify({"result": True}), 200

if __name__ == '__main__':
    app.run(debug=True)
