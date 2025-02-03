FROM python:2.7-slim
WORKDIR /app
COPY . .
CMD ["python", "main.py"]