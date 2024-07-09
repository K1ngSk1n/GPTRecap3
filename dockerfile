# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Make port 8008 available to the world outside this container
EXPOSE 8008

# Define environment variable
ENV FLASK_APP=run.py

# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8008", "--timeout", "300", "run:app"]
