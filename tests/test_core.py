import unittest
import xmlrunner
from app.app import meu_web_app


class TestHome(unittest.TestCase):

    def setUp(self):
        app = meu_web_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_html_string_response(self):
        self.assertEqual("ok", self.response.data.decode('utf-8'))

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

