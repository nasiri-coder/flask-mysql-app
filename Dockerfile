# Image de base
FROM python:3.10-slim

# Installer MySQL client pour tests éventuels
RUN pip install --no-cache-dir mysql-connector-python flask

# Copier le code
WORKDIR /app
COPY app/ /app

# Exposer le port
EXPOSE 5000

# Lancer Flask
CMD ["python", "app.py"]
