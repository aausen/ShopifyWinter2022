"""Model for Shopify Image Repo app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Image(db.Model):
    """Images in the database"""

    __tablename__ = "images"

    image_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    image_name = db.Column(db.String)
    image_self = db.Column(db.String)

    def __repr__(self):
        return f"<Image image_id = {self.image_id}, image_name = {self.image_name}, image = {self.image_self}>"

def connect_to_db(flask_app, db_uri='postgresql:///shopify-images', echo = True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    connect_to_db(app)