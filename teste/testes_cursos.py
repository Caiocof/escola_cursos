from rest_framework.test import APITestCase
from django.urls import reverse

from escola.models import Curso


class CursoTestCase(APITestCase):

    def setUp(self):
        # LISTANDO AS ROTAS
        self.list_url = reverse('Cursos-list')

        self.curso_1 = Curso.objects.create(
            codigo_curso=f'CTT1',
            descricao=f'Curso de Test 1',
            nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso=f'CTT2',
            descricao=f'Curso de Test 2',
            nivel='B'
        )

    def test_fauil(self):
        self.fail('O teste falhou')
