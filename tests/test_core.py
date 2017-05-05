import unittest
from app.views import meu_web_app
import datetime
from dateutil.parser import parse


class TestHomeView(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_html_string_response(self):
        self.assertEqual("ok", self.response.data.decode('utf-8'))

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)


class TestDateView(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/date')

    def test_for_a_date(self):
        date = parse(self.response.data.decode('utf-8'))
        self.assertTrue(isinstance(date, datetime.datetime))
