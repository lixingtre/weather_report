APP := weather-report
shell:
	docker-compose exec  -e COLUMNS="`tput cols`" -e LINES="`tput lines`" $(APP) bash; 
build:
	docker-compose build; 
up:
	docker-compose up -d
down:
	docker-compose down
restart:
	docker-compose build; docker-compose down; docker-compose up -d

