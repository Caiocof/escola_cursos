from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
                  path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
                  path('servidor-django/', admin.site.urls),
                  path('', include(router.urls)),
                  path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
                  path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
