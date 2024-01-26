FROM python:3.12.1-slim-bookworm

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]
