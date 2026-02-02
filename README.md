# Configuration Management Demo App

## Problem Statement
Applications behave differently in different environments when
configuration values are hardcoded. This project demonstrates how
to externalize configuration and manage environments properly.

## Application
- Python Flask application
- Reads configuration using environment variables
- No hardcoded configuration values

## Configuration Management
- `.env` file used for local setup
- Environment variables used for Docker containers

## Environments
The application runs in:
- Development (`APP_ENV=dev`)
- Testing (`APP_ENV=test`)

Output changes based on the environment.

## Dockerization
- Dockerfile included
- Environment variables passed at runtime

## CI Pipeline
GitHub Actions pipeline includes:
- Build
- Test
- Docker build simulation

## Tools Used
- Python Flask
- GitHub
- GitHub Actions
- Docker (design only)
