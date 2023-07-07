import pytest
from .models import Categoria


# este decorador es para que lo teste pero no afecte a la base de datos
@pytest.mark.django_db
def test_get_categoria():
    nueva_categoria = Categoria.objects.create(
        nombre = 'categoria de test',
    )

    categoria = Categoria.objects.all()

    assert categoria.count() == 1
    assert categoria[0].nombre == nueva_categoria.nombre


@pytest.mark.django_db
def test_get_categorias():
    for x in range(20):
         nueva_categoria = Categoria.objects.create(
            nombre = 'otro test',
    )

    categoria = Categoria.objects.all()

    assert categoria.count() == 20
    assert categoria[0].nombre == 'Terror'
