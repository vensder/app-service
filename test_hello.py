from hello import myapp
import unittest

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = myapp.test_client()

    def test_main(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
        assert b'Welcome' in rv.data
        