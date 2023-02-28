# Use an official Node.js runtime as the base image for the build stage
FROM node:14-alpine AS build-stage

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install the required packages
RUN npm install --production

# Copy the rest of the application code to the working directory
COPY . .

# Build the React app for production
RUN npm run build

# Use an official Node.js runtime as the base image for the runtime stage
FROM node:14-alpine AS runtime-stage

# Set the working directory to /app
WORKDIR /app

# Copy the production-ready code from the build stage to the working directory
COPY --from=build-stage /app/build ./build

# Install serve to run the production-ready code
RUN npm install -g serve

# Specify the command to run when the container starts
CMD ["serve", "-s", "build", "-l", "3000"]