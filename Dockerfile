# Use official Python image from Docker Hub
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your script and dependencies
COPY index.py /app/

# (Optional) Install any dependencies here
 RUN pip install -r requirements.txt

# Command to run your Python script
CMD ["python", "index.py"]
