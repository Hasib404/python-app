#Set base eimage
FROM python

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local source directory to the working directory
COPY src/ .

# Command to run on the container start
CMD ["python", "./app.py"]