# Use the official Python Alpine image as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies and the dns_validate package
RUN pip3 install --no-cache-dir .

# Specify the command to run on container start
ENTRYPOINT ["dns_validate"]
