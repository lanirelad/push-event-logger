
# Use the official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /workingDir

# Copy the Python script into the container
ADD . /workingDir

# install requirements
RUN pip install -r requirements.txt 

# Run app
ENTRYPOINT ["sh", "-c", "python main.py"]