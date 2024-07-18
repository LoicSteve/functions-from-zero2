install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov==calCli --cov=mylib test_*.py

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py mylib/*.py
	
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 441525731509.dkr.ecr.eu-west-3.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 441525731509.dkr.ecr.eu-west-3.amazonaws.com/logistics:latest
	docker push 441525731509.dkr.ecr.eu-west-3.amazonaws.com/logistics:latest

all: install format lint test deploy