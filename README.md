# Task Assignment Project

## Overview

This is a Task Assignment project built using Python, Django, HTML, and Bootstrap. The project allows users to create, assign, and manage tasks efficiently. It includes user authentication, task creation, task assignment, and task status tracking features.

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete tasks
- Assign tasks to users
- Track task status (to do, in progress, completed)
- Responsive design using Bootstrap

## Technologies Used

- Python
- Django (backend framework)
- HTML (markup language)
- Bootstrap (front-end framework)

## Setup Instructions

### Prerequisites

- Python 3.x
- Django 3.x
- pip (Python package installer)
- A virtual environment (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:vaddi4144/mysite.git

    cd mysite
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000` to see the application running.

## Project Structure

