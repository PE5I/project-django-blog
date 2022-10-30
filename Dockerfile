# Pull base iamge
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /djangoblog

# Install dependencies 
COPY Pipfile Pipfile.lock /djangoblog/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /djangoblog/