FROM python:3.10.5-slim-bullseye

RUN mkdir wd
WORKDIR /wd

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir resources
COPY ./resources/configuration.json ./resources

COPY src/ ./

CMD exec gunicorn --workers=2 --threads=2 -b :$PORT main:vApp