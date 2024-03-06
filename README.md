# Student Progress Tracker

## Description

The Student Progress Tracker is a Django-based web application designed for educational institutions to collect and analyze student progress data. It offers a user-friendly interface for students to submit their progress, while administrators can access analysis tools to visualize and analyze the data.

## Project Structure

```plaintext
django-project/
├── Web/                           # Django project directory
│   ├── __init__.py                # Initialization file
│   ├── asgi.py                    # ASGI config for deploying with ASGI servers
│   ├── settings.py                # Django settings file
│   ├── urls.py                    # URL routing configuration
│   └── wsgi.py                    # WSGI config for deployment
├── main/                          # Django app directory
│   ├── migrations/                # Directory for database migrations
│   ├── static/                    # Directory for static files (CSS, JS, etc.)
│   │   └── style.css              # Example CSS file
│   ├── templates/                 # Directory for HTML templates
│   │   ├── about.html             # HTML template for the "About" page
│   │   ├── create.html            # HTML template for the data collection form
│   │   ├── index.html             # HTML template for the homepage
│   │   └── thankyou.html          # HTML template for the thank you page
│   ├── __init__.py                # Initialization file
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py                    # Configuration for the app
│   ├── forms.py                   # Form definitions for the app
│   ├── models.py                  # Database models for the app
│   └── tests.py                   # Test cases for the app
├── db.sqlite3                     # SQLite database file
└── manage.py                      # Django's command-line utility for administrative tasks
```



## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage

- Visit the homepage to access the data submission form.
- Administrators can access analysis tools through the admin panel (/admin) to visualize and analyze student progress data.

## Contributing

Contributions are welcome! Follow the GitHub flow for making contributions.

## License

This project is licensed under the MIT License.
