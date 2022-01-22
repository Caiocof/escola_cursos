from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from escola.models import Aluno


class AlunosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Alunos-list')

        self.aluno_1 = Aluno.objects.create(
            nome='Aluno teste1',
            rg='999999999',
            cpf='11111111111',
            data_nascimento='2022-02-02',
            celular='77988888888',
        )
        self.aluno_2 = Aluno.objects.create(
            nome='Aluno teste2',
            rg='888888888',
            cpf='222222222222',
            data_nascimento='2022-02-02',
            celular='77988888888',
        )

    def test_get_alunos(self):
        """Testando o GET all alunos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_post_alunos(self):
        """Testando o POST em alunos"""
        data = {
            'nome': 'Aluno teste3',
            'rg': '888888888',
            'cpf': '22222222221',
            'data_nascimento': '2022-02-02',
            'celular': '77988888888',
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_put_alunos(self):
        """Testando o PUT em alunos"""
        data = {
            'nome': 'Aluno 13',
            'rg': '888877777',
            'cpf': '45679812355',
            'data_nascimento': '2020-02-01',
            'celular': '8899995555'
        }

        response = self.client.put('/alunos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_delete_alunos(self):
        """Testando o DELETE em alunos"""
        response = self.client.delete('/alunos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
