-include .env

.PHONY: run
run:
	- docker network create $(TG_LINK_NETWORK)
	- sleep 1
	- docker build -t $(TG_LINK_DB_IMAGE_NAME) -f db.Dockerfile .
	- docker build -t $(TG_LINK_MIGRATIONS_IMAGE_NAME) -f migrations.Dockerfile .
	- docker build -t $(TG_LINK_TG_IMAGE_NAME) -f tg_bot.Dockerfile .
	- docker build -t $(TG_LINK_SITE_IMAGE_NAME) -f site.Dockerfile .
	- docker-compose up
