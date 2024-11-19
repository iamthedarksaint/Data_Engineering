# Use a lightweight Python image as the base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /api

# Copy only the requirements file to leverage Docker's caching
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Make the start script executable
RUN chmod +x start_app.sh

# Expose the port FastAPI will run on (must match the port in docker-compose.yml)
EXPOSE 8000

# Command to run the FastAPI application
CMD ["./start_app.sh"]