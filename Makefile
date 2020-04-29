.SILENT:

test:
	docker run --rm -t \
		-v $$PWD:/app -w /app \
		python:3-alpine \
		sh -c 'pip install -r ./requirements.txt && pytest'
.PHONY: test
