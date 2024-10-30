# Gift Shop Website

A full-featured gift shop website built with Django. This application includes product listing, a shopping cart, and an order management system. Users can browse gifts, add items to their cart, and complete purchases.

## Features

- **Product Catalog**: View a variety of gift items with detailed descriptions, prices, and images.
- **Shopping Cart**: Add items to the cart, update quantities, and view the total cost.
- **Order Management**: Place orders and view order history.
- **User Authentication**: Sign up, log in, and manage user profile and orders.
- **Admin Panel**: Manage products, categories, and orders.

## Getting Started

### Prerequisites

- **Python**: Make sure Python (>= 3.6) is installed.
- **Django**: This project is built with Django 4.x.
- **MySQL**: Install MySQL and set up a database for this project.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/giftshop.git
   cd giftshop
2. **Set Up Virtual Environment**:
   python -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate

3. **Install Django and Other Requirements:**
   pip install django mysqlclient

4. **Database Configuration: In settings.py, set up your database:**
   DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'giftshop_db',
          'USER': 'yourusername',
          'PASSWORD': 'yourpassword',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }

7. **Run Migrations:**
   python manage.py makemigrations
   python manage.py migrate
   
8. **Create a Superuser:**
   python manage.py createsuperuser

9. **Collect Static Files:**
  python manage.py collectstatic

10. **Run the Development Server:**
    python manage.py runserver

# Project Structure
giftshop/
├── manage.py
├── README.md
├── shop/                 # Main application
│   ├── models.py         # Database models
│   ├── views.py          # Application views
│   ├── templates/        # HTML templates
│   ├── static/           # Static files (CSS, JS, images)
│   └── forms.py          # Django forms for user input
├── static/
└── templates/



