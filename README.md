# Basic Tasks Manager

**A beginner-friendly task manager built while learning Flask.**

Basic Tasks Manager is a simple CRUD web application for creating, viewing, editing, and deleting tasks. The project was created as a practical introduction to Flask routes, HTML templates, form handling, SQLAlchemy models, and SQLite database operations.

## Features

- Add new tasks
- View tasks in creation order
- Edit existing tasks
- Delete tasks
- Store task data in a local SQLite database
- Style the interface with SCSS

## Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/)
- [SCSS](https://sass-lang.com/)

## Run Locally

### Prerequisites

- Python 3.12 or newer
- `pip` or [uv](https://docs.astral.sh/uv/)

### Using a Virtual Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/xxArcandisxx/Basic-Tasks-Manager.git
   cd Basic-Tasks-Manager
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install flask flask-scss flask-sqlalchemy
   ```

4. Start the Flask application:

   ```bash
   python app.py
   ```

5. Open the local app in your browser:

   - http://127.0.0.1:5000/

### Using uv

The project also includes `pyproject.toml` and `uv.lock`:

```bash
uv sync
uv run python app.py
```

## How It Works

The application uses a `Task` SQLAlchemy model with fields for task content, completion state, and creation time. Flask routes handle the main CRUD operations:

- `GET /` — display tasks
- `POST /` — create a task
- `GET /edit/<id>` — show the edit form
- `POST /edit/<id>` — update a task
- `GET /delete/<id>` — delete a task

The SQLite database is created locally when the application starts. Since local database files are ignored by Git, each developer can use their own development data.

## Project Structure

```text
Basic-Tasks-Manager/
├── app.py              # Flask application, routes, and database model
├── static/style.scss   # SCSS styles
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Locked uv dependencies
└── .gitignore          # Ignored development files
```

## What This Project Teaches

This project is intended for learning and experimenting with:

- Creating a Flask application
- Defining routes and handling HTTP methods
- Reading form data with `request.form`
- Rendering pages with Jinja templates
- Building database models with SQLAlchemy
- Creating, querying, updating, and deleting records
- Serving a local web application during development

## Development Notes

- The application currently runs with Flask debug mode enabled for local learning.
- The database uses SQLite and is stored locally by Flask.
- Do not use the development server or default configuration for production deployments.

## License

No license has been specified for this project yet.
