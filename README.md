# Todo Application API Documentation

This API provides functionalities for user registration, login, and managing todo tasks.

## Authentication

### Register User

- URL: `/register/`
- Method: `POST`
- Description: Registers a new user.
- Request Body:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- Response:
  - Status Code: `201 Created` on success, `400 Bad Request` on failure

### Login User

- URL: `/login/`
- Method: `POST`
- Description: Logs in an existing user.
- Request Body:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- Response:
  - Status Code: `200 OK` on success with access and refresh tokens, `400 Bad Request` on failure

### Access Tokens

- URL: `/token/`
- Method: `POST`
- Description: Obtains access tokens.
- Response: Access and refresh tokens

### Refresh Tokens

- URL: `/token/refresh/`
- Method: `POST`
- Description: Refreshes access tokens.
- Response: New access token

## Todo Tasks

### Create Todo Task

- URL: `/api/todos/`
- Method: `POST`
- Description: Creates a new todo task.
- Request Body:
  ```json
  {
    "name": "string",
    "description": "string (optional)",
    "deadline": "string (optional)"
  }
  ```
- Response:
  - Status Code: `201 Created` on success, `400 Bad Request` on failure

### List Todo Tasks

- URL: `/api/todos/`
- Method: `GET`
- Description: Retrieves a list of todo tasks for the authenticated user.
- Response:
  - Status Code: `200 OK` on success

### Retrieve Todo Task

- URL: `/api/todos/{todo_id}/`
- Method: `GET`
- Description: Retrieves details of a specific todo task.
- Response:
  - Status Code: `200 OK` on success

### Update Todo Task

- URL: `/api/todos/{todo_id}/`
- Method: `PUT`
- Description: Updates details of a specific todo task.
- Request Body:
  ```json
  {
    "name": "string (optional)",
    "description": "string (optional)",
    "deadline": "string (optional)"
  }
  ```
- Response:
  - Status Code: `200 OK` on success, `400 Bad Request` on failure

### Delete Todo Task

- URL: `/api/todos/{todo_id}/`
- Method: `DELETE`
- Description: Deletes a specific todo task.
- Response:
  - Status Code: `204 No Content` on success

## Models

### Todo Model

- `user`: ForeignKey to User model (authenticated user)
- `name`: Name of the todo task (string)
- `description`: Description of the todo task (string, optional)
- `deadline`: Deadline of the todo task (datetime, optional)
- `created_at`: Date and time when the task was created (auto-generated)
- `modified_at`: Date and time when the task was last modified (auto-generated)
