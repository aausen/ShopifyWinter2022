"""CRUD operations"""

from model import Image, db, connect_to_db

def create_image(image_name):
    """Create and return a new image."""

    image = Image(image_name = image_name)

    db.session.add(image)
    db.session.commit()

    return image

def get_all_images():
    """Get all the images from the database."""

    return Image.query.all()

def delete_image_from_db(image_id):
    """Delete an image."""

    del_image = Image.query.filter(Image.image_id == image_id).first()
    db.session.delete(del_image)
    db.session.commit()

    if __name__ == '__main__':
        from server import app
        connect_to_db(app)