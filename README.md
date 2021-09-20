# ShopifyWinter2022
A project for the Shopify Winter 2022 Backend Internship

# Tech Stack
- Python
- Flask
- PostgreSQL
- SQLAlchemy
- HTML
- Jinja
- CSS

# Features

Users can upload their own images to the application. Once they are uploaded, they can view 
all of the uploaded images. Users are also able to delete images.

# How to Install Shopify Winter Challenge 2022

## Clone repository
Clone my github repo onto your local machine

``git clone https://github.com/aausen/ShopifyWinter2022.git``

## Create a virtual enviroment
`` virtualenv env ``

## Activate your virutal enviroment
`` source env/bin/activate ``

## Install requirements
`` pip install -r requirements.txt ``


## Save your Flask secret key in ``secrets.sh`` in the following format:

`` export secret_key="YourSecretKey" ``

## Source your key from your ``secrets.sh`` file to your virtual env

`` source secrets.sh ``

## Create your database

`` createdb shopify-images ``

``python3 -i model.py ``

``  >> db.create_all() ``

## Run the application

`` python3 server.py ``

## View in browser

Click the given link to localhost:5000 to view and run in your browser.


