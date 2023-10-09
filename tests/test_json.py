import unittest
from flask import jsonify
from uuid import uuid4

from lenticular_cloud.app import create_app
from lenticular_cloud.model import User

class TestBasicJsonFunction(unittest.TestCase):



    def test_encode(self):
        app = create_app()
        uuid = uuid4()
        with app.app_context():
            text = jsonify(uuid)
            print(text)
