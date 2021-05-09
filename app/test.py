from flask import Flask
from werkzeug.utils import get_content_type
from flask_testing import TestCase
from db import db, app
import unittest

class FlaskTestCases(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        print(response)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()