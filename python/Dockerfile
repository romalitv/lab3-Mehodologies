FROM python:3.10.11-buster

LABEL version="1.1"

WORKDIR /app

COPY requirements/backend.in .

RUN pip install --no-cache-dir -r backend.in

RUN pip install numpy

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]