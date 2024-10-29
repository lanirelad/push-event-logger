
# Use the official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /workingDir

# Copy the Python script into the container
COPY . /workingDir

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Run app
ENTRYPOINT ["sh", "-c", "python main.py"]