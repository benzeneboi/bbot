# Use an official Node.js runtime as the base image
FROM node:14-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the package.json file to the working directory
COPY package*.json .

# Install the required packages
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Specify the command to run when the container starts
CMD ["npm", "start"]
