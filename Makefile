
.DEFAULT_GOAL:=help
.PHONY: help

# -- CONFIGS --

APP_NAME=kabum
VERSION=latest
PORT=5000

##@ Database preparation
create-db:
	rm -f mock.db
	python load_mock_db.py

##@ Run with Python
dev: create-db dev-prep dev-run  ## Setup and start Python backend locally

dev-prep:  ## Install Python dependencies
	pip install -r requirements.txt

dev-run:  ## Start Flask backend server
	FLASK_APP=app.py FLASK_ENV=developement FLASK_DEBUG=True flask run

##@ Run with Docker
docker: create-db docker-build docker-run ## Build docker image and Run the container

docker-build: ## Build Docker Image
	docker build --tag $(APP_NAME):$(VERSION) .

docker-run: ## Run Docker Container
	docker run -ti --rm -p $(PORT):5000 \
	--name $(APP_NAME) $(APP_NAME):$(VERSION)

docker-sh: ## Start Bash session in container
	docker exec -ti $(APP_NAME) bash

##@ Helpers
help:  ## Display help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage:\n  make \033[36m<target>\033[0m\n"} /^[0-9a-zA-Z_-]+:.*?##/ \
		 { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
