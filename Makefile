run:
	docker-compose run web python manage.py migrate
	docker-compose up --build