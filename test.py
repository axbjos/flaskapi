#!/usr/bin/env python3
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Axnet IoT Temperature API')

    def test_recent_temps(self):
        rv = self.app.get('/recent_temps/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Recent Bed Room Temps')

if __name__ == '__main__':
    unittest.main()
