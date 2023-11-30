# Vendor Management System

This is a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

# Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/vendor-management-system.git
cd vendor-management-system
```
### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```
### 6. Run Development Server

```bash
python manage.py runserver
```
The server will be running at http://127.0.0.1:8000/.

# API Endpoints

### Vendor Profile Management

```bash
Create a new vendor: POST /api/vendors/
List all vendors: GET /api/vendors/
Retrieve a specific vendor's details: GET /api/vendors/{vendor_id}/
Update a vendor's details: PUT /api/vendors/{vendor_id}/
Delete a vendor: DELETE /api/vendors/{vendor_id}/
```
### Purchase Order Tracking

```bash
Create a purchase order: POST /api/purchase_orders/
List all purchase orders: GET /api/purchase_orders/
Retrieve details of a specific purchase order: GET /api/purchase_orders/{po_id}/
Update a purchase order: PUT /api/purchase_orders/{po_id}/
Delete a purchase order: DELETE /api/purchase_orders/{po_id}/
```
### Vendor Performance Evaluation

```bash
Retrieve a vendor's performance metrics: GET /api/vendors/{vendor_id}/performance
```
### Acknowledge Purchase Order

```bash
Acknowledge a purchase order: POST /api/purchase_orders/{po_id}/acknowledge
```

# Superuser Access
To access the Django admin panel for data management:
```bash
Visit http://127.0.0.1:8000/admin/
Log in with the superuser credentials created during the setup.
```
To run the test suite follow below cmd
```bash
python manage.py test vendor_app.tests
```
