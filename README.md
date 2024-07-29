# wotmers-agritech

# WOTMERS WEB APPLICATION

WOTMERS WEB APPLICATION is a comprehensive agricultural web app aimed at transforming farming practices and boosting productivity in Nigeria and Africa. The app provides features such as user registration and profiles, marketplace, weather forecasts, expert advice and support, educational resources, financial services, data analytics, and government and NGO integration.

## Project Setup

### Prerequisites

- Python 3.x
- Django 3.x or 4.x
- Django REST framework

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/wotmers-agritech.git
    cd wotmers-agritech
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

4. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Models

### Category

- `name` (CharField): The name of the category.

### Product

- `name` (CharField): The name of the product.
- `price` (DecimalField): The price of the product.
- `description` (TextField): The description of the product.
- `category` (ForeignKey): The category the product belongs to.
- `image` (ImageField): An optional image of the product.

## Views

### Category Views

- `category_list`: 
  - `GET`: Returns a list of all categories.
  - `POST`: Creates a new category.
- `category_detail`: 
  - `GET`: Returns details of a specific category.

### Product Views

- `product_list`: 
  - `GET`: Returns a list of all products.
  - `POST`: Creates a new product.
- `product_detail`: 
  - `GET`: Returns details of a specific product.

## Serializers

### CategorySerializer

Serializes the `Category` model.

### ProductSerializer

Serializes the `Product` model, including nested `Category` data.

## URLs

- `categories/`: 
  - `GET`: List all categories.
  - `POST`: Create a new category.
- `categories/<int:pk>/`: 
  - `GET`: Retrieve details of a specific category.
- `products/`: 
  - `GET`: List all products.
  - `POST`: Create a new product.
- `products/<int:pk>/`: 
  - `GET`: Retrieve details of a specific product.

