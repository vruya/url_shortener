## Run project environment under docker-compose
docker-compose up --build
## Run tests and follow steps in file urlstore/tests.py
docker-compose run web python manage.py test
