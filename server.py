"""Server for Shopify Image Repository"""

from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from model import connect_to_db, db
import crud
import os

app = Flask(__name__)
app.secret_key = os.environ['secret_key']
ALLOWED_EXTENTIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_filename(filename):
    return "." in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    print('getting stuck')
    if request.method == 'POST':
        print('getting stuck 1')
        if 'file' not in request.files:
            print('getting stuck 2')
            flash("No file part.")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('getting stuck 3')
            flash('No selected file.')
            return redirect(request.url)
        if file and allowed_filename(file.filename):
            print('getting stuck 4')
            filename = secure_filename(file.filename)
            crud.create_image(filename)
            flash('Image added')
            return render_template('index.html')
    return render_template("index.html")

@app.route("/")
def show_index():
    """View index."""

    return render_template("index.html")




if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug = True)