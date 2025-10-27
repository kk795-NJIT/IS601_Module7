# QR Code Generator - Docker Assignment

A containerized Python application that generates QR codes from URLs using Docker.

## Quick Start with DockerHub

The image is already built and available on DockerHub! Pull and run directly:

```bash
docker run -d --name qr-generator kk795/qr-code-generator-app
```

**DockerHub Repository**: https://hub.docker.com/r/kk795/qr-code-generator-app

## Features

- Generates QR codes from URLs
- Saves QR codes as PNG images
- Supports environment variables for configuration
- Runs as a non-root user for security
- Comprehensive logging

## Prerequisites

- Docker 20.10+
- DockerHub account (for pushing images)
- Git

## Installation

### 1. Install Docker

Follow the official Docker installation guide: https://docs.docker.com/get-started/

Verify installation:
```bash
docker --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
```

## Building the Docker Image

Build the Docker image locally:

```bash
docker build -t qr-code-generator-app .
```

## Running the Container

### Default Usage

Run with the default URL:
```bash
docker run -d --name qr-generator qr-code-generator-app
```

### Custom URL

Override the URL with a custom one:
```bash
docker run -d --name qr-generator \
  qr-code-generator-app --url http://www.njit.edu
```

### With Volume Mounting

Mount a local directory to access generated QR codes:
```bash
docker run -d --name qr-generator \
  -v /path/to/local/qr_codes:/app/qr_codes \
  qr-code-generator-app --url http://github.com/kaw393939
```

### Environment Variables

You can also use environment variables:
```bash
docker run -d --name qr-generator \
  -e QR_CODE_URL="http://example.com" \
  -e QR_OUTPUT_DIR="/app/qr_codes" \
  qr-code-generator-app
```

## Checking Container Logs

View the container logs:
```bash
docker logs qr-generator
```

Follow logs in real-time:
```bash
docker logs -f qr-generator
```

## Stopping and Cleaning Up

Stop the container:
```bash
docker stop qr-generator
```

Remove the container:
```bash
docker rm qr-generator
```

## Pushing to DockerHub

### 1. Login to DockerHub

```bash
docker login
```

Enter your DockerHub username and password when prompted.

### 2. Tag Your Image

```bash
docker tag qr-code-generator-app your-dockerhub-username/qr-code-generator-app
```

### 3. Push to DockerHub

```bash
docker push your-dockerhub-username/qr-code-generator-app
```

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow that:
- Builds the Docker image on every push to `main`
- Runs tests inside a container
- Pushes the image to DockerHub (requires secrets configuration)

### Setting Up GitHub Secrets

To enable automatic pushing to DockerHub, add these secrets to your GitHub repository:

1. Go to Settings > Secrets and variables > Actions
2. Add `DOCKERHUB_USERNAME` - your DockerHub username
3. Add `DOCKERHUB_TOKEN` - your DockerHub access token

## Security Features

- **Non-Root User**: The application runs as the `myuser` non-root user
- **Minimal Base Image**: Uses `python:3.12-slim-bullseye` for reduced attack surface
- **Directory Ownership**: Logs and QR codes directories are owned by `myuser`
- **No Cache Installation**: Uses `--no-cache-dir` for pip to reduce image size

## Project Structure

```
.
├── Dockerfile                 # Docker image definition
├── .dockerignore              # Files excluded from Docker build
├── main.py                    # QR Code Generator application
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── REFLECTION.md              # Assignment reflection
└── .github/workflows/         # GitHub Actions workflows
    └── docker-build-push.yml
```

## Application Usage

The application accepts command-line arguments:

```bash
python main.py --url <URL> --output <OUTPUT_DIR>
```

Arguments:
- `--url`: URL to encode in the QR code (default: http://github.com/kaw393939)
- `--output`: Directory to save QR codes (default: qr_codes)

## Logging

Application logs are stored in the `logs/` directory with timestamps:
- Filename format: `qr_generator_YYYYMMDD_HHMMSS.log`
- Logs are also printed to stdout

## Troubleshooting

### Container exits immediately
Check the logs to see the error:
```bash
docker logs qr-generator
```

### Permission denied errors
Ensure the output directory has proper permissions:
```bash
docker exec qr-generator ls -la qr_codes/
```

### Image not found
Rebuild the image:
```bash
docker build -t qr-code-generator-app .
```

## License

MIT

## Author

Created for IS601 Module 7 - Docker Assignment
