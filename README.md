# Order Management System (Django + DRF + Google OAuth 2.0)

## Overview
This project is a template for an Order Management System using Django Rest Framework (DRF) as the backend, with Google OAuth 2.0 authentication. It provides endpoints for data entry and retrieval, protected by OAuth authentication.

## Features
- Google OAuth 2.0 authentication (access & refresh tokens)
- Protected API endpoints for adding and retrieving orders
- Filter orders by title or user

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/harshkushwaha7x/Y_work.git
cd <project-directory>
```

### 2. Create and Activate Virtual Environment
```
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Configure Google OAuth
- Create a project and OAuth 2.0 credentials in the [Google Cloud Console](https://console.developers.google.com/).
- Set the following environment variables in a `.env` file at the project root:
```
SOCIAL_AUTH_GOOGLE_CLIENT_ID=your-google-client-id
SOCIAL_AUTH_GOOGLE_SECRET=your-google-client-secret
```

### 5. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (optional, for admin access)
```
python manage.py createsuperuser
```

### 7. Run the Development Server
```
python manage.py runserver
```

## API Usage

### Authentication
- Use `/api/auth/login/` and `/api/auth/registration/` for login/registration.
- For Google OAuth, use `/api/auth/social/login/` with provider `google` (see dj-rest-auth docs for details).

### Orders API
- **POST /api/orders/**: Add a new order (fields: `title`, `description`).
- **GET /api/orders/**: Retrieve orders for the authenticated user. Filter by `title` using query params.

#### Example: Add Order
```
POST /api/orders/
Authorization: Token <your-token>
{
  "title": "Sample Order",
  "description": "Order details here."
}
```

#### Example: Get Orders
```
GET /api/orders/?title=Sample
Authorization: Token <your-token>
```

## Security Notes
- All sensitive keys are loaded from environment variables.
- API endpoints are protected and only accessible to authenticated users.

## Documentation
- Code is documented and follows Django/DRF best practices.
- See source files for further details.

---

For any issues, please refer to the documentation or contact the maintainer. 
