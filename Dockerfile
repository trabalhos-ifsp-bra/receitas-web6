FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev
RUN pip install -U pip setuptools
COPY requirements/base.txt /code/base.txt
COPY requirements/local.txt /code/requirements.txt
RUN pip install -r /code/base.txt
RUN pip install -r /code/requirements.txt
EXPOSE 8000
ADD . /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

##  Comandos Ativação Docker
##  docker build -t django .
##  docker run -p 8000:8000 --name receitas django

##  Atualizar Imagem
##  docker stop receitas
##  docker rm receitas
##  docker build -t django .
##  docker run -p 8000:8000 --name receitas django
