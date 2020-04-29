.SILENT:

test:
	docker run --rm -t \
		-v $$PWD:/app -w /app \
		python:3-alpine \
		sh -c 'pip install -r ./requirements.txt && pylint *.py && pytest'
.PHONY: test

watch:
	docker run --rm -t \
		-v $$PWD:/app -w /app \
		python:3-alpine \
		sh -c 'pip install -r ./requirements.txt && pytest-watch --beforerun "pylint *.py"'
.PHONY: watch
