# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Make the response directory writable
RUN mkdir -p /app/response && chmod 777 /app/response

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
