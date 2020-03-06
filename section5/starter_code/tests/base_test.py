"""
BaseTest

This class should be the parent class to each no unit class.
It allows for instantiation for database dynamically and makes sure
that database is blank each time.
"""

from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # get test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()