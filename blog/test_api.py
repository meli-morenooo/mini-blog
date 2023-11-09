import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# Credenciales existentes en la base de datos
EXISTING_USERNAME = 'admin'
EXISTING_PASSWORD = 'admin'

# Fixture para autenticar al cliente con las credenciales existentes
@pytest.fixture
@pytest.mark.django_db
def authenticated_client():
    client = APIClient()
    client.login(username=EXISTING_USERNAME, password=EXISTING_PASSWORD)
    yield client

# Función para obtener una URL de lista de la API
def get_list_url(view_name):
    return reverse(view_name + '-list')

@pytest.mark.django_db
def test_access_protected_views(authenticated_client):  # Asegúrate de que este fixture esté correctamente definido
    # Definir las vistas protegidas que deseas probar
    views_to_test = ['usuario-list', 'categoria-list', 'post-list', 'comentario-list']

    for view_name in views_to_test:
        # Obtener la URL de lista
        list_url = reverse(view_name)

        # Intentar acceder a la URL con autenticación
        response = authenticated_client.get(list_url)

        # Verificar que la respuesta sea exitosa y contenga datos
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_access_unauthorized_views():
    # Definir las vistas protegidas que deseas probar
    views_to_test = ['usuario-list', 'categoria-list', 'post-list', 'comentario-list']

    for view_name in views_to_test:
        # Obtener la URL de lista
        list_url = reverse(view_name)

        # Intentar acceder a la URL sin autenticación
        response = APIClient().get(list_url)

        # Verificar que la respuesta sea un código 401 (no autorizado)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED