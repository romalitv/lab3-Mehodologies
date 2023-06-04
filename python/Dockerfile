FROM python:3.10-alpine

LABEL version="1.1"

WORKDIR /app

RUN apk add --no-cache \
    python3-dev \
    build-base \
    && pip install --upgrade pip

COPY requirements/backend.in .

RUN pip install --no-cache-dir -r backend.in

RUN apk add --no-cache \
    g++ \
    && pip install numpy

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]