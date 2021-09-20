"""Data to populate test db."""

from model import Image, db

def example_data():
    """Creating some sample data."""
    
    first = Image(image_id=1, image_name="first image")
    second = Image(image_id=2, image_name="second image")
    third = Image(image_id=3, image_name="third image")
    fourth = Image(image_id=4, image_name="fourth image")

    db.session.add_all([first, second, third, fourth])
    db.session.commit()

