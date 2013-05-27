import json

from models.user_model import User
from testing.base_case import BaseTestCase
from testing.fixtures import user_fixtures


class AuthHandlersTestCase(BaseTestCase):

    def test_find_user_valid(self):
        username = "ericc"
        rv = self.app.get('/user/validate', query_string={'username': username})
        rv_dict = json.loads(rv.data)
        self.assertEqual('success', rv_dict['status'])
        self.assertTrue(rv_dict['valid'])
        self.assertIsNone(rv_dict['message'])

    def test_find_user_already_exists(self):
        user = user_fixtures.factory()
        rv = self.app.get('/user/validate',
                          query_string={'username': user.username})
        rv_dict = json.loads(rv.data)
        self.assertEqual('success', rv_dict['status'])
        self.assertFalse(rv_dict['valid'])

    def test_register(self):
        registration_form = {
            'username': 'ericc',
            'email': 'eric@example.com',
            'password': 'abc123'
        }
        rv = self.app.post('/register',
                           data=registration_form,
                           follow_redirects=True)
        user = User.objects.get(username=registration_form['username'])

        self.assertIn('Logged in as %s.' % registration_form['username'],
                      rv.data)
        self.assertEqual(registration_form['username'], user.username)
        self.assertEqual(registration_form['email'], user.email)

    def test_login_username(self):
        password = "abc123"
        user = user_fixtures.factory(password=password)
        login_form = {
            'username_or_email': user.username,
            'password': password
        }
        rv = self.app.post('/login',
                           data=login_form,
                           follow_redirects=True)
        self.assertIn('Logged in as %s.' % user.username,
                      rv.data)
