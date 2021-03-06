from rest_framework import viewsets, generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer
from escola.serializer import AlunoSerializerV2
from escola.serializer import CursoSerializer
from escola.serializer import MatriculaSerializer
from escola.serializer import ListaMatriculasAlunoSerializer
from escola.serializer import ListaAlunosMatriculadosSerializer

from escola.response_locate import create_locate


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AlunoSerializerV2
        else:
            return AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    http_method_names = ['get', 'post', 'put', 'path']

    def create(self, request):
        serialize = self.serializer_class(data=request.data)
        return create_locate(serialize, request)


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ['get', 'post', 'put']

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(*args, **kwargs)

    def create(self, request):
        serialize = self.serializer_class(data=request.data)
        return create_locate(serialize, request)


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
