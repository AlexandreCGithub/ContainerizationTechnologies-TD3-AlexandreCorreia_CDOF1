# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY app.py .

# Spécifier la version de NumPy
RUN pip install numpy==1.21.0

CMD ["python", "app.py"]
