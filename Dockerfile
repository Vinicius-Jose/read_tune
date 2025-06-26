FROM python:3.10.18-slim-bullseye

WORKDIR /app

COPY . /app

RUN pip install poetry \
    && poetry install --without dev \
    && poetry run python manage.py collectstatic --noinput \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

EXPOSE 8080

CMD ["poetry", "run","uvicorn", "playlist.asgi:application", "--host", "0.0.0.0","--port", "8080"]

