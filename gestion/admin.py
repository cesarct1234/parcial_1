from django.contrib import admin
from .models import Alumno, Profesor, Materia, Curso, Matricula

# Registrar modelos en el panel de administración
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Materia)
admin.site.register(Curso)
admin.site.register(Matricula)
