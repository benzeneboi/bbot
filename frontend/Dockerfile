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
FROM nginx:1.21.0-alpine as production

ENV NODE_ENV production

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=build-stage /app/build .

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD [ "nginx", "-g", "daemon off;" ]