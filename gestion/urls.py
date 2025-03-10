from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlumnoViewSet, ProfesorViewSet, MateriaViewSet, CursoViewSet, MatriculaViewSet
from .views import UserViewSet

router = DefaultRouter()
router.register(r'alumnos', AlumnoViewSet)
router.register(r'profesores', ProfesorViewSet)
router.register(r'materias', MateriaViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)
router.register(r'usuarios', UserViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
