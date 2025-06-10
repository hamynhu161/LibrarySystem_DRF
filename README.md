# Library System API

This is a Django REST Framework (DRF) project to manage a simple library system. It includes APIs for managing books, customers, and book loans.

## Features

    -   Manage books with fields like title, author, ISBN, and availability  

    -   Manage customers with contact details  

    -   Manage book loans and automatically update book availability  

    -   API endpoints to list, create, update, and delete records  

## Setup

    -   Clone the reponsitory

    -   Create a virtual environment

        python -m venv venv </br>

        venv\Scripts\activate

    -   Install dependencies

        pip install -r requirements.txt

    -   Apply migrations

        python manage.py makemigrations </br>

        python manage.py migrate