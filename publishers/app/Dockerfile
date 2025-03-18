FROM python:3.9-slim

WORKDIR /app

COPY ../../publishers /app/publishers
COPY ../../consumers /app/consumers
COPY ../../common /app/common

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python"]
