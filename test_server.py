"""Test suite for testing server."""

from flask import Flask
import server
import unittest
import crud
import model
from test_data import example_data



class MyAppIntegrationTestCase(unittest.TestCase):
    """Integration tests: testing Flask server."""

    def setUp(self):
        print("(setUp ran)")
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True
        server.app.config['SECRET_KEY'] = 'key'

        # with self.client as c:
        #     with c.session_transaction() as sess:
        #         sess['user_id'] = 1
                

        model.connect_to_db(server.app, "postgresql:///test_shopify")

        model.Image.query.delete()

        model.db.create_all()
        example_data()

        

    def tearDown(self):
        print("(tearDown ran)")
        return 

    def test_index(self):
            result = self.client.get("/")
            self.assertEqual(200, result.status_code)

  

if __name__ == '__main__':
    unittest.main()