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

    #add two more tests please
    #duplicate the class above blah blah

class TestGetOne(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        rv = self.app.get('/get_one_temp_api')
        self.assertEqual(rv.status, '200 OK')

class Test404(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        rv = self.app.get('/idontexist')
        self.assertEqual(rv.status, '404 NOT FOUND')


if __name__ == '__main__':
    unittest.main()
