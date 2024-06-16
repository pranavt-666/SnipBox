# SnipBox

SnipBox is a Django-based backend API for a short note saving app with tagging functionality.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pranavt-666/SnipBox

## Install dependencies:

pip install -r requirements.txt


## Apply database migrations:  
python manage.py migrate

## Run the development server: 
python manage.py runserver

## Access the API:

The development server will start at http://localhost:8000.

## Requirements
Ensure you have the following Python packages installed (versions specified):

```bash
asgiref==3.8.1
Django==5.0.6
djangorestframework==3.15.1
djangorestframework-simplejwt==5.3.1
PyJWT==2.8.0
sqlparse==0.5.0
typing_extensions==4.12.2
tzdata==2024.1
```

##  Postman Documentation
For detailed API documentation and test cases, refer to the [Postman Documentation.](https://documenter.getpostman.com/view/36353426/2sA3XQi3BF)

## Database Schema
![Database Schema](Database%20Schema.png)