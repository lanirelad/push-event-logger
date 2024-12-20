
# Use the official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /workingDir

# Copy the Python script into the container
# ADD . /workingDir
COPY . . 
# install requirements
RUN pip install --no-cache-dir --timeout=100 -r requirements.txt

# Run app
ENTRYPOINT ["python", "main.py"]