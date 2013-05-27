import unittest

from app import app
from app import db


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        # assert using test db before dropping
        db_name = app.config['MONGODB_SETTINGS']['DB']
        assert db_name.startswith('test')
        db.connection.drop_database(db_name)
