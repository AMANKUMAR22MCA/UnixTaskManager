# Use official lightweight Python image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    python3-dev \
    build-base \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    postgresql-client

# Install Python dependencies
COPY requirements.txt . 
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Install Gunicorn (make sure it's in requirements.txt too)
RUN pip install gunicorn

# Expose port
EXPOSE 8000

# Command to run the app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "task_manager.wsgi:application"]
