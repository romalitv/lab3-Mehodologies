FROM python:3.10.11-buster

LABEL version="1.1"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements/backend.in

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]