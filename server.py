"""Server for Shopify Image Repository"""

from flask import Flask, render_template, request
from model import connect_to_db, db
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']






if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug = True)