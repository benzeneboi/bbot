FROM python:3.10-alpine

# set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the folder
COPY . .

# start the server
#CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
