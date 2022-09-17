# Tea coffee shop

----

## Summary

Requirements:
- Python: version 3.10
- Libraries:
  - Development
    - `requirements/development.txt`
  - Production
    - `requirements/base.txt`

Source repositories:
- Backend — 
- Mobile - 

----

## Development

### Running a local version of the project:

Activate the virtual environment:
```
source /<env dir>/bin/activate
```

#### You need to configure the environment variables, an example is in _dockerfiles/app/sample.local.env

Run migrate
```
python manage.py migrate
```

Run django server
```
python manage.py runserver
```


----
## Docker

### Running a local version of the project in a docker container:

Build and run docker images:
```
docker-compose build 
docker-compose up
```

Run migrate:
```
docker-compose run app python manage.py migrate
```

Create superuser:
```
docker-compose run app createsuperuser
```

To connect to running container:
```
docker-compose exec app /bin/bash
```