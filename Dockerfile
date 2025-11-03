FROM python:3.10-slim

RUN pip install --no-cache-dir flask mysql-connector-python

WORKDIR /app
COPY app/ /app

EXPOSE 5000
CMD ["python", "app.py"]
