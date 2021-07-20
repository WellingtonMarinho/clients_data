FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements-dev.txt /app/
COPY requirements.txt /app/

# RUN apt-get update && apt-get install -y \
#     openssh-client \
#     git \
#     gdal-bin \
#     python3-gdal
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app/