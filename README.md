# Modern CRM System

A user-friendly Customer Relationship Management (CRM) system built with Django and MySQL.

## Features

-   👥 User Authentication (Login/Register)
-   👤 Client Management (Add/View/Edit/Delete)
-   🔍 Search and Filter Capabilities
-   📱 Responsive Design
-   🎨 Modern UI with Bootstrap

## Quick Start

1. Install Python 3.8 or higher
2. Set up MySQL database:

    ```bash
    mysql -u root -p
    # Enter your MySQL password
    CREATE DATABASE crmdb;
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create admin user:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

Visit http://localhost:8000 to access the application.

## Test Data

To populate the system with test data:

1. Install additional requirements:

    ```bash
    pip install Faker
    ```

2. Create a test user and dummy data:
    ```bash
    python manage.py create_dummy_data
    ```

This will create:

-   Test user (username: testuser, password: testpass123)
-   50 sample clients
-   Random orders for each client

## Search Features

The CRM includes comprehensive search functionality:

-   Search by client name, email, phone, city, or state
-   Real-time filtering of results
-   Pagination of search results
-   Export search results to CSV (admin interface)

## Tech Stack

-   Backend: Django 5.1
-   Database: MySQL
-   Frontend: Bootstrap 5
-   Icons: Font Awesome
-   Fonts: Inter (Google Fonts)

## License

MIT License
