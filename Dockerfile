# Use Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy files
COPY index.py /app/
COPY requirements.txt /app/  
# Copy the rest of the files

# Install dependencies if any
RUN test -f requirements.txt && pip install -r requirements.txt || echo "No requirements to install"

# Run the script
CMD ["python", "index.py"]
