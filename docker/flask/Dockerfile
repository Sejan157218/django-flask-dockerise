FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /flask
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /flask
