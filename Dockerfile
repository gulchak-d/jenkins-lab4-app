FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install Flask
CMD ["python", "app.py"]
