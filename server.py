"""Server for Shopify Image Repository"""

from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from model import connect_to_db, db
import crud
import os
from jinja2 import StrictUndefined

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENTIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.secret_key = os.environ['secret_key']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_filename(filename):
    return "." in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS

@app.route("/", methods=['GET', 'POST'])
def upload_file():

    all_img = crud.get_all_images()

    single_image = []
    for item in all_img:
        image_id = item.image_id
        image_name = item.image_name

        single_image.append((image_id, image_name))

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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            crud.create_image(filename)
            flash('Image added')
            return render_template('index.html', 
                                    single_image = single_image)
    return render_template("index.html", 
                            single_image = single_image)

@app.route("/delete", methods=["POST"])
def delete():
    """Delete image."""

    image_id = request.form.get("delete-img")

    crud.delete_image_from_db(image_id)

    return redirect('/')




if __name__ == '__main__':
    connect_to_db(app)

    app.run(host='0.0.0.0', debug = True)