##  Comandos Ativação Docker
##  docker build -t django .
##  docker run -p 8000:8000 --name receitas django

##  Atualizar Imagem
##  docker stop receitas
##  docker rm receitas
##  docker build -t django .
##  docker run -p 8000:8000 --name receitas django

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements/base.txt /code/base.txt
COPY requirements/production.txt /code/production.txt
COPY requirements/local.txt /code/local.txt

RUN pip install -r base.txt
RUN pip install -r local.txt

ENV DB_NAME receitasdb
ENV DB_PASS faltatompero
ENV DB_USER chef

COPY . /code/
