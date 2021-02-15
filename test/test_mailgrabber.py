import unittest
from mailgrabber import App

class AppTests(unittest.TestCase):
    
    def test_options(self):
        opt = ["app", "--mailserver=localhost"]
        app = App(opt)
        self.assertEqual(app.cfg['mailserver']['server'], "localhost")
