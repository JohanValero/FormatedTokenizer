FROM python:3.10.5-slim-bullseye

RUN mkdir wd
WORKDIR /wd

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir resources
COPY ./resources/configuration.json ./wd/resources

COPY src/ ./

CMD ["python3", "./main.py"]