# Basic Authentication API

This project contains a simple API with Basic Authentication implemented using Flask. It allows users to access various endpoints based on their authentication status.

## Getting Started

To set up and run the project, follow these steps:

1. Clone the repository:
git clone https://github.com/<username>/alx-backend-user-data.git
cd alx-backend-user-data/


2. Install the required dependencies:
   
   pip3 install -r requirements.txt


3. Start the API server:
   
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app


4. Use the API by making HTTP requests to the available endpoints.

## Endpoints

- `GET /api/v1/status`: Returns the status of the API.
- `GET /api/v1/unauthorized`: Raises a 401 error (Unauthorized) to test the error handler.
- `GET /api/v1/forbidden`: Raises a 403 error (Forbidden) to test the error handler.
- `GET /api/v1/users`: Returns a list of user objects after successful Basic Authentication.

## Authentication Mechanism

The API uses Basic Authentication to secure the endpoints. When making requests to protected endpoints, include an `Authorization` header with the value `Basic <base64_credentials>`, where `<base64_credentials>` is the Base64 encoded version of `email:password`.

## Class Structure

The project includes two classes for managing authentication: `Auth` and `BasicAuth`. The `Auth` class serves as a template for all authentication systems, and the `BasicAuth` class inherits from `Auth` to implement Basic Authentication.

## Task Implementation

This project includes multiple tasks, each with a specific objective. The tasks include:

1. Implementing error handlers for 401 (Unauthorized) and 403 (Forbidden) status codes.
2. Defining which routes do not require authentication based on excluded paths.
3. Creating a class to manage API authentication (`Auth` class).
4. Implementing Basic Authentication and handling Base64 encoded credentials.
This project is developed and maintained by [Nwodo Thomas](https://github.com/Nwodothomas>).


Please replace <username> with your GitHub username and update any other placeholder information as needed.
