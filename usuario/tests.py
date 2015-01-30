from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class BaseTestCase(TestCase):

    def setUp(self):
        self.client = APIClient(enforce_csrf_checks=True)
        self.email = 'testuser@test.com'
        self.name = 'test user'
        self.password = 'testing'

        self.url_auth = '/api/auth/token/'
        self.url_create = '/api/user/create/'
        self.url_public = "/api/user/{}"

    def create_account(self):
        data = {
            'email': self.email,
            'nombre': self.name,
            'password': self.password
        }
        self.client.post(self.url_create, data, format='json')

    def create_user(self, email, name, password):
        data = {
            'email': email,
            'nombre': name,
            'password': password
        }
        self.client.post(self.url_create, data, format='json')

    def login(self):
        self.data = {
            'email': self.email,
            'password': self.password
        }
        print(self.client.post(self.url_auth, self.data, format='json').data)


class CreateUsuarioTest(BaseTestCase):

    def test_create_account_minimun_fields(self):
        """
        Crear cuenta con los campos minimos obligatorios
        """
        data = {
            'email': self.email,
            'nombre': self.name,
            'password': self.password
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def test_create_account_email_duplicate(self):
        """
        Crear cuenta con un email existente
        """
        self.create_account()
        data = {
            'email': self.email,
            'nombre': self.name,
            'password': self.password
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

    def test_create_account_incomplete_fields(self):
        """
        Crear cuenta con los campos obligatorios incompletos
        """
        data = {
            'email': self.email,
            'password': self.password
        }
        response = self.client.post(self.url_create, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)


class ObtainJSONWebTokenTests(BaseTestCase):

    def test_jwt_login_json(self):
        """
        Ensure JWT login view using JSON POST works.
        """
        self.create_account()
        #client = APIClient(enforce_csrf_checks=True)

        self.data = {
            'email': self.email,
            'password': self.password
        }

        response = self.client.post(self.url_auth, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def test_jwt_login_json_incomplete_creds(self):
        """
        Ensure JWT login view using JSON POST fails
        if incomplete credentials are used.
        """
        self.create_account()
        #client = APIClient(enforce_csrf_checks=True)

        self.data = {
            'email': self.email
        }
        response = self.client.post(self.url_auth, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

    def test_jwt_login_json_bad_password(self):
        """
        Ensure JWT login view using JSON POST fails
        if bad credentials are used.
        """
        self.create_account()
        client = APIClient(enforce_csrf_checks=True)

        self.data = {
            'email': self.email,
            'password': '123456'
        }
        response = client.post(self.url_auth, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)


class PublicUsuarioTests(BaseTestCase):

    def test_public_usuario_not_authenticated(self):
        """
        Un usuario no autenticado no puede ver la info de un usuario registrado
        """
        self.create_user(name='Test 2', email='testuser2@test', password='testing')
        response = self.client.post(self.url_public.format('2'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)

    def test_public_usuario_authenticated(self):
        """
        Un usuario autenticado puede ver la info de un usuario registrado
        NOTA:No se porque demonios no quiere funcionar :/
        """
        self.create_account()
        self.login()

        self.create_user(name='Test 2', email='testuser2@test', password='testing')

        response = self.client.post(self.url_public.format('2'))
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        print(response.data)
