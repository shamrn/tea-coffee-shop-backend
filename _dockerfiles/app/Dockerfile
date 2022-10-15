FROM python:3.10.4
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install gettext for makemessages command
RUN apt update && apt install -y gettext binutils libproj-dev gdal-bin

# generating directories structure
RUN mkdir -p /app/code /app/requirements

# add rquirements files
ADD ./requirements /app/requirements

# update pip
RUN python -m pip install --upgrade pip

# fixed problem on Apple M1 Pro processors
RUN python -m pip install psycopg2-binary --no-binary psycopg2-binary

# install requirements
RUN pip install --no-cache-dir -r /app/requirements/base.txt && \
    pip install --no-cache-dir -r /app/requirements/local.txt

# set working directory
WORKDIR /app/code

# copy project in docker container
ADD . /app/code
