# 📐 MathMS

**MathMS** is a Python API service for performing common mathematical operations like computing factorials, generating Fibonacci sequences, while logging all API activity.

## 🚀 Setup

1. **Clone the repository**

```
git clone <repo-url>
cd MathMS
```

2. **Initialize the Virtual Environment**

```
cd backend
python -m venv .venv
```

3. **Activate the Virtual Environment:**

- **Windows**
  `.venv\Scripts\activate`
- **Linux/macOS**
  `source .venv/bin/activate`

4. **Install all the dependecies**
   `cd ..`
   `pip install -r requirements.txt`

## ⚙️ Development & Task Automation

On Windows - use the provided `scripts.py` for common tasks.

```
py scripts.py start-server  # Start FastAPI server
py scripts.py test          # Run all tests in backend/tests
py scripts.py lint          # Lint with flake8
py scripts.py sort-imports  # Sort imports with isort
py scripts.py format        # Sort imports and lint
```

💡 For Unix-based systems, consider `cat scripts.py` and running manually.

## 📡 API Usage

- **Factorial**
  - `POST /math/factorial` with `{ "number": 5 }`
    returns `{ "result": 120 }`
- **Fibonacci**
  - `POST /math/fibonacci` with `{ "number": 7 }`
    returns `{ "sequence": [0, 1, 1, 2, 3, 5, 8] }`
- **Logs**
  - `GET /logs` returns a list of all API requests logged into the database.

## 🧱 Project Structure

```
backend/
    controllers/        # API routes
    models/             # Database Models
    schemas/            # Schemas for business logic
    services/           # Business logic
    utils/              # Helpers
    tests/              # Test files
    main.py             # Entry point
    requirements.txt    # Package requirements
scripts.py              # Common tasks (Windows)
```

## 🧰 Tools and Technologies

- **Python 3.12+**
- **FastAPI** — Web framework for building APIs
- **Uvicorn** — ASGI server for FastAPI
- **Pydantic** — Data validation and serialization
- **SQLite** — Lightweight database for logging
- **pytest** — Unit testing framework
- **flake8** — Linting and code style checks
- **isort** — Import sorting
- **Virtualenv** — Isolated Python environment
- **subprocess, pathlib** — Used in utility scripts for automation

## 🐳 Containerization (Docker)

### Files

- **`Dockerfile`** — builds the FastAPI app into a Python 3.12 slim container.
- **`.dockerignore`** — excludes cache, `.venv`, `.git`, etc.

### Commands

```bash
docker build -t mathms:latest .
docker run --rm -p 8000:8000 mathms:latest
```

---

## ☸️ Orchestration (Kubernetes)

### Manifests (`manifest/`)

**`mathematics.yaml`**

### Apply

```bash
kubectl apply -f k8s/
```

### Access

- Port-forward:

```bash
kubectl -n mathms port-forward svc/mathms-svc 8080:8080
```
