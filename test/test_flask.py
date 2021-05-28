#from unittest import TestCase

from app import create_app
from pytest import fixture


@fixture
def flask_test(scope='class'):
    """Roda antes de todos os testes"""
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()
    app.client = app.test_client()
    app.db.create_all()

    yield app
    app.db.drop_all()

# class TestFlaskBase(class):
#     def setUp(self):
#         """Roda antes de todos os testes"""
#         self.app = create_app()
#         self.app.testing = True
#         self.app_context = self.app.test_request_context()
#         self.app_context.push()
#         self.client = self.app.test_client()
#         self.app.db.create_all()
#
#
#     def tearDown(self):
#         """Roda depois de todos os testes."""
#         self.app.db.drop_all()

