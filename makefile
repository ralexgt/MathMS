.PHONY: setup-unix setup-win setup-win-bash \
		start-server lint sort-imports format

# Setup for Linux/macOS 
setup-unix:
	cd backend && \
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt

# Setup for Windows (CMD or PowerShell)
setup-win:
	cd backend && \
	py -m venv .venv && \
	.venv\Scripts\activate && \
	py -m pip install --upgrade pip && \
	py -m  pip install -r requirements.txt

# Setup for Windows (Bash)
setup-gitbash:
	cd backend && \
	py -m venv .venv && \
	. .venv/Scripts/activate && \
	py -m pip install --upgrade pip && \
	py -m pip install -r requirements.txt

# Start the FastAPI server (Windows with Bash)
start-server:
	cd backend && \
	. .venv/Scripts/activate && \
	py -m uvicorn main:app

# Lint with flake8 (Windows with Bash)
lint:
	cd backend && \
	. .venv/Scripts/activate && \
	py -m flake8 . --exclude=.venv,__pycache__,build,dist

# Sort imports with isort (Windows with Bash)
sort-imports:
	cd backend && \
	. .venv/Scripts/activate && \
	py -m isort . --skip .venv

# Format all (sort imports + lint check)
format: sort-imports lint