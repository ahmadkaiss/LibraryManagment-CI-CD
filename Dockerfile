# Use an official Python image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install pytest

#install other dependencies in requirements.txt
COPY requirments.txt .
RUN pip install -r requirments.txt

# Default command to run tests
RUN pytest -v

CMD ["python", "book_functions.py"]
