FROM python:3.9-slim

WORKDIR /app

COPY ../../publishers /app
COPY ../../consumers /app
COPY ../../common /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python"]
