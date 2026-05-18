# Base Image
FROM python:3.11

# Set Working Directory
WORKDIR /app

# Copy Files
COPY . .

# Install Dependencies
RUN pip install -r requirements.txt

# Expose Flask Port
EXPOSE 5000

# Run Flask App
CMD ["python", "app.py"]