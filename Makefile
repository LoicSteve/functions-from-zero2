install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=mylib test_*.py

format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py mylib/*.py
	
container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
deploy:
#echo "deploy not implemented"

all: install format lint test deploy