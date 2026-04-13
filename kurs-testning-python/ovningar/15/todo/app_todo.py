# app_todo.py
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
todos = []
next_id = 1

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>TODO-app</title></head>
<body>
    <h1>Mina uppgifter</h1>
    <form method="POST" action="/add">
        <input type="text" id="task-input" name="task"
               placeholder="Ny uppgift..." required>
        <button type="submit" id="add-btn">Lägg till</button>
    </form>
    <ul id="todo-list">
        {% for todo in todos %}
        <li data-testid="todo-item-{{ todo.id }}"
            class="{{ 'done' if todo.done else '' }}">
            <span class="task-text">{{ todo.task }}</span>
            <a href="/toggle/{{ todo.id }}" data-testid="toggle-{{ todo.id }}">
                {{ '✅' if todo.done else '⬜' }}
            </a>
            <a href="/delete/{{ todo.id }}" data-testid="delete-{{ todo.id }}">
                🗑️
            </a>
        </li>
        {% endfor %}
    </ul>
    <p id="count">{{ todos|length }} uppgifter</p>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, todos=todos)

@app.route("/add", methods=["POST"])
def add():
    global next_id
    task = request.form.get("task", "").strip()
    if task:
        todos.append({"id": next_id, "task": task, "done": False})
        next_id += 1
    return redirect(url_for("index"))

@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
