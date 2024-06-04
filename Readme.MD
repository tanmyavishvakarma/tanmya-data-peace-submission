# User Management API

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/tanmyavishvakarma/tanmya-data-peace-submission.git
    cd tanmya-data-peace-submission
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run the server:

    ```
    python manage.py runserver
    ```

## API Endpoints

### List Users

- **URL**: `/api/users`
- **Method**: `GET`
- **Query Parameters**:
  - `page`: Page number for pagination
  - `limit`: Number of items per page (default: 5)
  - `name`: Search users by name (substring match, case-insensitive)
  - `sort`: Attribute to sort by (prefix with `-` for descending order)
- **Sample Query**: `/api/users?page=1&limit=10&name=Josephine&sort=-age`

### Create a New User

- **URL**: `/api/users`
- **Method**: `POST`
- **Request Payload** (JSON):

    ```json
    {
        "first_name": "Josephine",
        "last_name": "Darakjy",
        "company_name": "Chanay, Jeffrey A Esq",
        "city": "Brighton",
        "state": "MI",
        "zip": 48116,
        "email": "josephine_darakjy@darakjy.org",
        "web": "http://www.chanayjeffreyaesq.com",
        "age": 48
    }
    ```

### Get User Details

- **URL**: `/api/users/{id}`
- **Method**: `GET`
- **Sample Query**: `/api/users/1`

### Update User Details

- **URL**: `/api/users/{id}`
- **Method**: `PUT`
- **Request Payload** (JSON):

    ```json
    {
        "first_name": "Josephine",
        "last_name": "Darakjy",
        "age": 48
    }
    ```

### Delete a User

- **URL**: `/api/users/{id}`
- **Method**: `DELETE`
- **Sample Query**: `/api/users/1`

## Postman Instructions

1. **Install Postman**: If you don't have Postman installed, download and install it from [here](https://www.postman.com/downloads/).

2. **Create a New Collection**: In Postman, create a new collection for organizing your API requests.

3. **Add Requests**:
    - Follow the endpoint details provided above to create GET, POST, PUT, and DELETE requests in Postman.

4. **Send Requests**: Use the `Send` button in Postman to test the API endpoints.
