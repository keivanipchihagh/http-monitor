FROM registry.keivanipchihagh.ir/python:3.10-slim

ENV DockerHome=/home/services

RUN apt-get update
RUN apt-get clean
RUN apt-get autoremove
RUN apt-get install curl -y

# create the working directory
RUN mkdir -p ${DockerHome}

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV DOCKER_BUILDKIT=1

COPY requirements.txt ${DockerHome}

WORKDIR ${DockerHome}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy the working directory
COPY . ${DockerHome}