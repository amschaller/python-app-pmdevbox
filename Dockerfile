# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN \
	apt-get update && \
	pip install --trusted-host pypi.python.org -r requirements.txt && \
	apt-get install -y iputils-ping


# Run app.py when the container launches
CMD ["python", "sensortest.py"]
# CMD ["sleep","100000"]
