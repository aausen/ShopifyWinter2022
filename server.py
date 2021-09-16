"""Server for Shopify Image Repository"""

from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from model import connect_to_db, db
import crud
import os
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.secret_key = os.environ['secret_key']
ALLOWED_EXTENTIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_filename(filename):
    return "." in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS

@app.route("/", methods=['GET', 'POST'])
def upload_file():

    all_img = crud.get_all_images()

    single_image = []
    for item in all_img:
        img_id = item.image_id
        img_name = item.image_name

        single_image.append((img_id, img_name))

    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file part.")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file.')
            return redirect(request.url)
        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)
            crud.create_image(filename)
            flash('Image added')
            return render_template('index.html', 
                                    single_image = single_image)
    return render_template("index.html", 
                            single_image = single_image)

# @app.route("/")
# def show_index():
#     """View index."""

#     all_img = crud.get_all_images()

#     single_image = []
#     for item in all_img:
#         img_id = item.image_id
#         img_name = item.image_name

#         single_image.append((img_id, img_name))

#     return render_template("index.html", 
#                             single_image = single_image)




if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug = True)