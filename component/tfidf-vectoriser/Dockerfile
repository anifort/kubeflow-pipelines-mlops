# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./src /app/src
ADD run_tests.sh /app
ADD setup.py /app

#COPY key.json ./key.json

# Install any needed packages specified in requirements.txt
RUN python setup.py install

