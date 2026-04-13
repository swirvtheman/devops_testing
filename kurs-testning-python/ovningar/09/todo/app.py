"""
TODO-app för Övning 9 — Explorativ testning.

Applikationen är skriven av Claude från Antrophic 2026.

Starta: python app.py
Gå till: http://localhost:5000
"""

from flask import Flask, request, redirect, url_for, render_template_string, jsonify
import datetime

app = Flask(__name__)

# In-memory storage
todos = []
next_id = 1

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TODO-appen</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 { margin-bottom: 20px; color: #2c3e50; }
        .stats {
            background: #fff;
            padding: 12px 16px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            display: flex;
            gap: 20px;
            font-size: 14px;
            color: #666;
        }
        .add-form {
            background: #fff;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            display: flex;
            gap: 10px;
        }
        .add-form input[type="text"] {
            flex: 1;
            padding: 10px 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
        }
        .add-form select {
            padding: 10px 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
        }
        .add-form button {
            padding: 10px 20px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }
        .add-form button:hover { background: #2980b9; }
        .filter-bar {
            margin-bottom: 16px;
            display: flex;
            gap: 8px;
        }
        .filter-bar a {
            padding: 6px 14px;
            border-radius: 16px;
            text-decoration: none;
            font-size: 13px;
            background: #e0e0e0;
            color: #555;
        }
        .filter-bar a.active {
            background: #3498db;
            color: white;
        }
        .todo-list { list-style: none; }
        .todo-item {
            background: #fff;
            padding: 14px 16px;
            border-radius: 8px;
            margin-bottom: 8px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .todo-item.done { opacity: 0.6; }
        .todo-item.done .todo-title { text-decoration: line-through; }
        .todo-title { flex: 1; font-size: 16px; }
        .todo-priority {
            font-size: 11px;
            padding: 2px 8px;
            border-radius: 10px;
            font-weight: 600;
        }
        .priority-hög { background: #fee; color: #c0392b; }
        .priority-medel { background: #fff3e0; color: #e67e22; }
        .priority-låg { background: #e8f5e9; color: #27ae60; }
        .todo-date { font-size: 12px; color: #999; }
        .todo-actions { display: flex; gap: 6px; }
        .todo-actions a, .todo-actions button {
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 12px;
            text-decoration: none;
            border: 1px solid #ddd;
            background: #fff;
            cursor: pointer;
            color: #555;
        }
        .todo-actions a:hover, .todo-actions button:hover {
            background: #f0f0f0;
        }
        .btn-delete { color: #e74c3c !important; border-color: #e74c3c !important; }
        .empty { text-align: center; color: #999; padding: 40px; }
        .search-form {
            margin-bottom: 16px;
        }
        .search-form input {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
            width: 100%;
        }
        .edit-form input[type="text"] {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
            width: 60%;
        }
        .flash {
            padding: 10px 16px;
            border-radius: 6px;
            margin-bottom: 16px;
            font-size: 14px;
        }
        .flash-success { background: #d4edda; color: #155724; }
        .flash-error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>📝 TODO-appen</h1>

    {% if message %}
    <div class="flash flash-{{ message_type }}">{{ message }}</div>
    {% endif %}

    <div class="stats">
        <span>Totalt: {{ total }}</span>
        <span>Klara: {{ done }}</span>
        <span>Kvar: {{ remaining }}</span>
    </div>

    <form class="add-form" action="/add" method="POST">
        <input type="text" name="title" placeholder="Lägg till en ny uppgift..." autofocus>
        <select name="priority">
            <option value="medel">Medel</option>
            <option value="hög">Hög</option>
            <option value="låg">Låg</option>
        </select>
        <button type="submit">Lägg till</button>
    </form>

    <form class="search-form" action="/" method="GET">
        <input type="text" name="search" placeholder="Sök bland uppgifter..."
               value="{{ search_query }}">
    </form>

    <div class="filter-bar">
        <a href="/" class="{{ 'active' if filter == 'alla' }}">Alla</a>
        <a href="/?filter=aktiva" class="{{ 'active' if filter == 'aktiva' }}">Aktiva</a>
        <a href="/?filter=klara" class="{{ 'active' if filter == 'klara' }}">Klara</a>
    </div>

    {% if edit_todo %}
    <div class="todo-item">
        <form class="edit-form" action="/edit/{{ edit_todo.id }}" method="POST"
              style="display:flex;gap:10px;align-items:center;flex:1;">
            <input type="text" name="title" value="{{ edit_todo.title }}">
            <select name="priority">
                <option value="hög" {{ 'selected' if edit_todo.priority == 'hög' }}>Hög</option>
                <option value="medel" {{ 'selected' if edit_todo.priority == 'medel' }}>Medel</option>
                <option value="låg" {{ 'selected' if edit_todo.priority == 'låg' }}>Låg</option>
            </select>
            <button type="submit">Spara</button>
            <a href="/">Avbryt</a>
        </form>
    </div>
    {% endif %}

    <ul class="todo-list">
    {% for todo in todos %}
        <li class="todo-item {{ 'done' if todo.done }}">
            <a href="/toggle/{{ todo.id }}">
                {{ '☑' if todo.done else '☐' }}
            </a>
            <span class="todo-title">{{ todo.title }}</span>
            <span class="todo-priority priority-{{ todo.priority }}">
                {{ todo.priority }}
            </span>
            <span class="todo-date">{{ todo.created }}</span>
            <div class="todo-actions">
                <a href="/?edit={{ todo.id }}">Redigera</a>
                <a href="/delete/{{ todo.id }}" class="btn-delete">Ta bort</a>
            </div>
        </li>
    {% endfor %}
    </ul>

    {% if not todos and not edit_todo %}
    <div class="empty">Inga uppgifter att visa. Lägg till en ovan!</div>
    {% endif %}

</body>
</html>
"""


@app.route("/")
def index():
    global todos

    filter_type = request.args.get("filter", "alla")
    search_query = request.args.get("search", "")
    edit_id = request.args.get("edit", type=int)
    message = request.args.get("msg")
    message_type = request.args.get("msg_type", "success")

    filtered = todos

    # Sökfunktion
    if search_query:
        filtered = [t for t in filtered if search_query in t["title"]]

    # Filtrering
    if filter_type == "aktiva":
        filtered = [t for t in filtered if not t["done"]]
    elif filter_type == "klara":
        filtered = [t for t in filtered if t["done"]]

    # Statistik
    total = len(todos)
    done = len([t for t in todos if t["done"]])
    remaining = len([t for t in todos if t["done"]])  # <-- BUG: ska vara "not t['done']"

    edit_todo = None
    if edit_id:
        edit_todo = next((t for t in todos if t["id"] == edit_id), None)

    return render_template_string(
        HTML_TEMPLATE,
        todos=filtered,
        total=total,
        done=done,
        remaining=remaining,
        filter=filter_type,
        search_query=search_query,
        edit_todo=edit_todo,
        message=message,
        message_type=message_type,
    )


@app.route("/add", methods=["POST"])
def add():
    global next_id
    title = request.form.get("title", "")
    priority = request.form.get("priority", "medel")

    todo = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.datetime.now().strftime("%Y-%m-%d"),
    }
    next_id += 1
    todos.append(todo)

    return redirect(url_for("index", msg="Uppgift tillagd!", msg_type="success"))


@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo:
        todo["done"] = not todo["done"]
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    global todos
    original_len = len(todos)
    todos = [t for t in todos if t["id"] != todo_id]

    if len(todos) < original_len:
        return redirect(
            url_for("index", msg="Uppgift borttagen!", msg_type="success")
        )
    else:
        return redirect(
            url_for("index", msg="Uppgiften hittades inte", msg_type="success")
        )


@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo:
        new_title = request.form.get("title", "")
        new_priority = request.form.get("priority", todo["priority"])
        todo["title"] = new_title
        todo["priority"] = new_priority
        return redirect(
            url_for("index", msg="Uppgift uppdaterad!", msg_type="success")
        )
    return redirect(
        url_for("index", msg="Uppgiften hittades inte", msg_type="error")
    )


# ---------- JSON API ----------

@app.route("/api/todos")
def api_list():
    """Lista alla todos som JSON."""
    return jsonify(todos)


@app.route("/api/todos", methods=["POST"])
def api_add():
    """Lägg till via JSON API."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Ingen JSON-data"}), 400

    global next_id
    title = data.get("title", "")
    priority = data.get("priority", "medel")

    todo = {
        "id": next_id,
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.datetime.now().strftime("%Y-%m-%d"),
    }
    next_id += 1
    todos.append(todo)
    return jsonify(todo)


@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def api_delete(todo_id):
    """Ta bort via JSON API."""
    global todos
    original = len(todos)
    todos = [t for t in todos if t["id"] != todo_id]
    if len(todos) < original:
        return jsonify({"message": "Borttagen"})
    return jsonify({"message": "Hittades inte"})


if __name__ == "__main__":
    # Lägg till lite exempeldata
    todos = [
        {
            "id": 1,
            "title": "Handla mat",
            "priority": "hög",
            "done": False,
            "created": "2025-01-15",
        },
        {
            "id": 2,
            "title": "Tvätta kläder",
            "priority": "medel",
            "done": True,
            "created": "2025-01-14",
        },
        {
            "id": 3,
            "title": "Läsa kurslitteratur",
            "priority": "hög",
            "done": False,
            "created": "2025-01-13",
        },
    ]
    next_id = 4
    print("=" * 50)
    print("  TODO-appen startar!")
    print("  Gå till: http://localhost:5000")
    print("  API: http://localhost:5000/api/todos")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000)
