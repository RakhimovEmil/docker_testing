install:
	pip3 install --requirement requirements.txt

run:
	docker-compose down
	docker-compose build
	docker-compose up
build:
	docker build . --tag emilrakhimov/lec12_server:1.0

start: build 
	docker run --detach --name server --publish 8080:8080 --rm emilrakhimov/lec12_server:1.0

stop:
	docker stop server
	
clean:
	rm -r __pycache__

healthcheck:
	@which docker || echo "docker is not installed"
	@which docker-compose || echo "docker-compose is not installed"

test:
	python3 -m unittest
