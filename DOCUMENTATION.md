# CRM System Technical Documentation

## System Architecture

### 1. Database Configuration

-   Located in `test_db.py` and `settings.py`
-   Uses MySQL with the following configuration:
    -   Host: localhost
    -   Port: 3306
    -   Database: crmdb
    -   User: root
    -   Password: admin

### 2. Core Components

#### Authentication System

-   Located in `webapp/views.py` and `webapp/forms.py`
-   Features:
    -   User registration with email verification
    -   Login/logout functionality
    -   Password reset capabilities
    -   Custom user forms with Bootstrap styling

#### Client Management

-   Models (`webapp/models.py`):

    -   Client model with fields:
        -   full_name
        -   email
        -   phone
        -   address
        -   city
        -   state
        -   zipcode
        -   created_at
        -   updated_at

-   Views (`webapp/views.py`):
    -   HomeView: Dashboard with client list
    -   ClientView: Detailed client information
    -   AddClientView: New client creation
    -   UpdateClientView: Edit client details
    -   DeleteClientView: Remove client records

#### Templates Structure

1. Base Template (`templates/base.html`):

    - Contains common layout elements
    - Responsive navigation
    - Bootstrap integration
    - Custom CSS styling

2. Client Templates:
    - `add_client.html`: Form for new clients
    - `client.html`: Detailed client view
    - `client_update.html`: Edit form
    - `home.html`: Dashboard/client list

### 3. URL Structure

-   Root URLs (`crm/urls.py`):

    -   Admin interface: `/admin/`
    -   Main application: `/`

-   Application URLs (`webapp/urls.py`):
    -   Home: `/`
    -   Client detail: `/client/<id>/`
    -   Add client: `/add-client/`
    -   Update client: `/update-client/<id>/`
    -   Delete client: `/delete-client/<id>/`

### 4. Forms (`webapp/forms.py`)

1. RegisterUserForm:

    - Username
    - Email
    - First name
    - Last name
    - Password
    - Password confirmation

2. AddClientForm:
    - All client fields with Bootstrap styling
    - Custom validation

### 5. Admin Interface

-   Custom admin views for Client model
-   Enhanced list display
-   Search functionality
-   Filtering options

### 6. Security Features

-   CSRF protection
-   User authentication required for all client operations
-   Secure password handling
-   MySQL native password authentication

### 7. Frontend Features

-   Responsive design
-   Modern UI components
-   Interactive tables
-   Modal confirmations
-   Form validation
-   Success/error messages

### 8. Database Migrations

All migrations are tracked in `webapp/migrations/`:

-   0001_initial.py: Base client model
-   0002_client_created_at.py: Added creation timestamp
-   0003_client_updated_at.py: Added update timestamp
-   0004_auto_update_datetime_fields.py: DateTime field updates
-   0005_alter_client_updated_at.py: Modified update field behavior

## File Dependencies

-   `settings.py` → Database configuration
-   `models.py` → Database structure
-   `views.py` → Business logic
-   `urls.py` → URL routing
-   `forms.py` → Form handling
-   Templates → User interface

## Maintenance

1. Database Backups:

    ```bash
    mysqldump -u root -p crmdb > backup.sql
    ```

2. Update Dependencies:

    ```bash
    pip freeze > requirements.txt
    ```

3. Run Tests:
    ```bash
    python manage.py test
    ```

## Troubleshooting

Common issues and solutions:

1. Database Connection:

    - Check MySQL service is running
    - Verify credentials in settings.py
    - Ensure database exists

2. Migration Issues:
    - Make migrations: `python manage.py makemigrations`
    - Apply migrations: `python manage.py migrate`
    - Reset migrations if needed: `python manage.py migrate --fake-initial`

## Search Implementation

The search functionality is implemented using:

1. Django Q objects for complex queries
2. Class-based ListView for efficient pagination
3. Real-time filtering in the database

### Search Fields

-   Client Name
-   Email
-   Phone
-   City
-   State

### Code Structure

```python
def get_queryset(self):
    queryset = Client.objects.all()
    search_query = self.request.GET.get('search', '')

    if search_query:
        queryset = queryset.filter(
            Q(full_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(city__icontains=search_query) |
            Q(state__icontains=search_query)
        )

    return queryset.order_by('-created_at')
```

## Data Export Features

The admin interface includes CSV export functionality:

-   Export selected clients
-   Include all client details
-   Include order summaries
-   Formatted for easy import into spreadsheet software
