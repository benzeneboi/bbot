#!/bin/bash

# Check if Docker is installed
if [ -x "$(command -v docker)" ]; then
    echo "Docker is not installed, installing it now."
    # Install Docker
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    # Remove installation script
    rm get-docker.sh
fi

# Build and run Dockerfile in current directory
docker-compose build
docker-compose up -d