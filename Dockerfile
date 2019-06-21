# Image used as base container
FROM python:3.6

# Output python is set straight to the termminal without buffering
ENV PYTHONUNBUFFERED 1

# Create root directory for the project in the container
RUN mkdir /website

# Set working directory
WORKDIR /website

COPY requirements.txt /website/
RUN pip install -r requirements.txt
ADD . /website/
