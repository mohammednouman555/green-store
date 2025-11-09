# Green Store - Django (MySQL) - Advanced (Ready to run)

## Overview
This is a ready-to-run Django project for a Green Store e-commerce site (plants, seeds, fertilizers, tools).
It includes:
- Product model (image support)
- Admin configuration for product & order management
- Session-based cart, checkout stub (for logged-in admin/demo users)
- Static templates and CSS
- MySQL configuration placeholders (set via environment variables or edit `greenstore/settings.py`)

## Requirements
- Python 3.12.4
- pip
- MySQL server (or compatible)
- Recommended Python packages (see `requirements.txt`)

## Setup (quick)
1. Unzip the project.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux / macOS
   venv\Scripts\activate     # Windows (PowerShell or cmd)
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a MySQL database and user. Then set environment variables (example):
   ```bash
   export GREENSTORE_DB_NAME=greenstore_db
   export GREENSTORE_DB_USER=your_db_user
   export GREENSTORE_DB_PASSWORD=your_db_password
   export GREENSTORE_DB_HOST=127.0.0.1
   export GREENSTORE_DB_PORT=3306
   export GREENSTORE_SECRET='some-secret-key'
   ```
   On Windows use `set` instead of `export`.

5. Apply migrations and create superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. (Optional) Add products via Django admin (http://127.0.0.1:8000/admin/).

7. Run the development server:
   ```bash
   python manage.py runserver
   ```
   Visit http://127.0.0.1:8000/ to view the site.

## Notes
- Payment integration is not included. Checkout marks an order and clears the cart; integrate Razorpay/Stripe in `store/views.checkout`.
- Images upload to `media/products/` — ensure `media/` exists and is writable.
- For production, set DEBUG=False and configure ALLOWED_HOSTS and static/media serving.

## Troubleshooting
- If you get `django.db.utils.OperationalError` for MySQL, ensure `mysqlclient` is installed and MySQL server is running.
- To install `mysqlclient` on Windows, use precompiled wheels or use `pip install mysqlclient` after having Visual C++ build tools.

## License
MIT
