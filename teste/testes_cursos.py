from rest_framework.test import APITestCase
from rest_framework import status
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
            nivel='A'
        )

    def test_requisicao_get_cursos(self):
        """Teste para verificar o GET all"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_cursos(self):
        """Teste para verificar o POST cursos"""
        data = {
            'codigo_curso': f'CTT3',
            'descricao': f'Curso de Test 3',
            'nivel': 'A'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_cursos(self):
        """Teste para verificar o DELETE do curso, o retorno esperado e False"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_cursos(self):
        """Teste para verificar o PUT de cursos"""
        data = {
            'codigo_curso': f'CTT1',
            'descricao': f'Curso de Test 6',
            'nivel': 'I'
        }

        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
