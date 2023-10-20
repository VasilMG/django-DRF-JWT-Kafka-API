# django-DRF-JWT-Postgres-API
Django API using - Django Rest Framework, JWT Auth, Postgres DB, Apache Kafka

## Table of Contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)

## Description

This is a Django Rest Framework project that includes JWT authentication using SimpleJWT and uses a PostgreSQL database. The project is designed to be run in Docker containers for ease of setup and deployment.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Installation

To run this project, follow these steps:

1. Clone this repository to your local machine. Navigate to the source directory of the project and run:

   ```bash
   docker-compose up -d
- if you are running Windows on your machine please make sure to uncomment the commands I've written in the Dockerfiles (kafka/Dockerfile) and the app's dockerfice ./Dockerfile
2. After that you will be able to access the app's documentation on localhost:8000/api/v1/swagger-schema/
3. During the installation process 2 users are created - you can see theri credentials in --> InterviewSystem/interview_app/management/commands/create_users.py
4. Choose a user and make a post request to localhost:8000/access/ to receive an access token or just use the swagger documentation to authenticate and make requests to the endpionts
5. Users can be created only through the django admin panel - you must run --> python manage.py createsuperuser  before you can access the admin panel at  localhost:8000/admin/
6. I have made a public endpoint /api/emails where we can see all the messages comming from Kafka brokers.

## Usage
After successfully installing the project, you can access the API and start making requests.

Access the API:

API base URL: http://localhost:8000/access/
<br>

## API Documentation
To access the API documentation, visit the Swagger schema:
API Documentation: http://localhost:8000/api/v1/swagger-schema/
- Make a post request with email and password of the pre-built users. You can find the users in interview_app/management/commands/create_users.py
- You will receive 2 tokens. Copy the value of 'access' token and go the the upper left button Authorize
- In the field FIRST type 'Bearer' followed by a space and THEN paste the value of the token. eg. Bearer <token_value>
- And you are good to go and make requests to the api. 

