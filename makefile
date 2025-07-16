.PHONY: setup-unix setup-win setup-win-bash

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
