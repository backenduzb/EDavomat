FROM python:3.13-alpine3.21

WORKDIR /app

COPY requirements.txt /app
COPY entrypoint.sh /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY project /app

EXPOSE 8000

ENTRYPOINT ["sh", "/app/entrypoint.sh"]