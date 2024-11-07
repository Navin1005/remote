# Use an official Python image as the base
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the entire project into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run your training script
CMD ["python", "src/train.py"]
