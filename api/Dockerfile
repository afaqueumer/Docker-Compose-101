# Dockerfile for FastAPI Application
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Create and set up a volume for the SQLite database
VOLUME /app/db

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]