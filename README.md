# 🏦 Bank Loan Management System

A comprehensive web-based loan management system built with Django that allows customers to apply for loans and enables bank managers to efficiently manage loan applications, approvals, and transactions.

**Author**: Sainath  
**Project Type**: Capstone Project  
**Year**: 2025

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [User Roles](#-user-roles)
- [API Endpoints](#-api-endpoints)
- [Database Schema](#-database-schema)
- [Contributing](#-contributing)
- [Deployment](#-deployment)
- [License](#-license)

## ✨ Features

### For Customers
- **User Registration & Authentication**: Secure signup and login system
- **Profile Management**: Create and update personal profile with profile picture
- **Loan Application**: Apply for various types of loans with detailed information
- **Loan Status Tracking**: View the status of loan applications (Pending, Approved, Rejected)
- **Loan History**: Access complete history of all loan applications
- **Transaction Management**: View and manage loan transactions

### For Bank Managers
- **Dashboard**: Comprehensive overview of all loan applications
- **Loan Approval/Rejection**: Review and process loan applications
- **Customer Management**: View and manage customer profiles
- **Loan Category Management**: Create and manage different types of loans
- **Interest Rate Management**: Set and update interest rates for loan categories
- **Transaction Monitoring**: Track all loan-related transactions
- **Reports**: Generate reports on loan activities

### General Features
- **Responsive Design**: Mobile-friendly interface
- **Security**: Secure authentication and authorization
- **File Upload**: Profile picture upload functionality
- **Search & Filter**: Advanced search and filtering options
- **Real-time Updates**: Dynamic status updates

## 🛠 Tech Stack

- **Backend**: Django 3.x (Python Web Framework)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 4
- **Database**: SQLite (Development), PostgreSQL (Production ready)
- **Authentication**: Django's built-in authentication system
- **File Storage**: Django's file handling system
- **Admin Interface**: Django Admin with Jazzmin theme
- **Deployment**: Heroku ready with Gunicorn

### Key Dependencies
All dependencies are listed in `requirements.txt` for easy installation:
- `django` - Web framework
- `django-jazzmin` - Enhanced Django admin interface
- `dj-database-url` - Database URL parsing
- `python-decouple` - Environment variable management
- `django-widget-tweaks` - Form field tweaks
- `django-cleanup` - Automatic file cleanup
- `django-bootstrap4` - Bootstrap integration
- `django-mathfilters` - Mathematical template filters
- `gunicorn` - WSGI HTTP Server for deployment
- `Pillow` - Python Imaging Library for image handling
- `psycopg2-binary` - PostgreSQL database adapter
- `whitenoise` - Static file serving for production
- `django-heroku` (for Heroku deployment only) - Heroku deployment configuration

## 🏗 System Architecture

```
Bank Loan Management System
├── loan_management_system/     # Main Django project
│   ├── settings.py            # Project settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py               # WSGI configuration
├── loginApp/                 # User authentication app
│   ├── models.py            # Customer user models
│   ├── views.py             # Authentication views
│   └── forms.py             # User forms
├── loanApp/                 # Loan management app
│   ├── models.py            # Loan-related models
│   ├── views.py             # Loan processing views
│   └── forms.py             # Loan forms
├── managerApp/              # Manager interface app
│   ├── models.py            # Manager-specific models
│   ├── views.py             # Manager dashboard views
│   └── forms.py             # Manager forms
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, Images)
└── media/                   # User uploaded files
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Bank-Loan-System.git
cd Bank-Loan-System
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv loan_env

# Activate virtual environment
# On macOS/Linux:
source loan_env/bin/activate
# On Windows:
loan_env\Scripts\activate
```

### Step 3: Install Dependencies
```bash
# Install all required packages from requirements.txt
pip install -r requirements.txt

# Note: For local development SQLite will be used
# If you plan to deploy to Heroku, you'll need PostgreSQL installed
# and uncomment the django-heroku line in requirements.txt
```

### Step 4: Database Setup
```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser
```

### Step 5: Collect Static Files
```bash
python manage.py collectstatic
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📖 Usage

### First Time Setup
1. Start the development server
2. Visit the admin panel at `/admin` and login with superuser credentials
3. Create loan categories (e.g., Personal Loan, Home Loan, Car Loan)
4. Set interest rates for each loan category

### Customer Workflow
1. **Register**: Create a new customer account
2. **Login**: Access the customer dashboard
3. **Profile**: Complete your profile information
4. **Apply**: Submit a loan application
5. **Track**: Monitor application status
6. **Manage**: View loan history and transactions

### Manager Workflow
1. **Login**: Access manager dashboard
2. **Review**: View pending loan applications
3. **Process**: Approve or reject applications
4. **Monitor**: Track all customer activities
5. **Manage**: Handle loan categories and settings

## 👥 User Roles

### Customer
- Can register and create profile
- Can apply for loans
- Can view loan status and history
- Can manage personal information

### Bank Manager/Admin
- Can access admin dashboard
- Can approve/reject loan applications
- Can manage loan categories
- Can view all customer data
- Can generate reports

## 🔗 API Endpoints

### Authentication
- `GET/POST /account/register/` - Customer registration
- `GET/POST /account/login-customer/` - Customer login
- `GET /account/logout/` - Logout

### Loan Management
- `GET/POST /loan/request/` - Create loan request
- `GET /loan/status/` - View loan status
- `GET /loan/history/` - Loan history
- `GET/POST /loan/transaction/` - Loan transactions

### Manager Interface
- `GET /manager/dashboard/` - Manager dashboard
- `GET /manager/applications/` - View all applications
- `POST /manager/approve/<id>/` - Approve loan
- `POST /manager/reject/<id>/` - Reject loan

## 🗄 Database Schema

### Key Models

#### CustomerSignUp
- `user` - OneToOne with Django User
- `first_name`, `last_name` - Customer name
- `email` - Contact email
- `address` - Customer address
- `profile_picture` - Profile image
- `designation` - Job designation
- `phone` - Contact number

#### loanCategory
- `loan_name` - Type of loan
- `interest_rate` - Interest rate for the loan
- `creation_date`, `updated_date` - Timestamps

#### loanRequest
- `customer` - Foreign key to CustomerSignUp
- `category` - Foreign key to loanCategory
- `amount` - Loan amount requested
- `year` - Loan duration in years
- `reason` - Purpose of loan
- `status` - Application status (pending/approved/rejected)

#### CustomerLoan
- Approved loan details
- Links customer to approved loan amount

#### loanTransaction
- Transaction history for loan payments
- Payment tracking and history

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

## 🚀 Deployment

### Heroku Deployment

The application is configured for easy Heroku deployment:

1. **Install Heroku CLI**
2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-app-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set DEBUG=False
   heroku config:set SECRET_KEY='your-secret-key'
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

6. **Run Migrations on Heroku**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Environment Variables
Create a `.env` file for local development:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Author**: Sainath  
**Copyright**: © 2025 Sainath



## 🙏 Acknowledgments

- **Author**: Sainath - *Initial work and development*
- Django community for the excellent framework
- Bootstrap for responsive design components

---

**Note**: This is a educational/demonstration project. For production use, ensure proper security measures, environment configuration, and testing procedures are in place.
