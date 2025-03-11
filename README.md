# parcial_1
# # Crear entorno virtual (opcional pero recomendado)


#python -m venv venv
# Activar el entorno virtual
# En Windows (CMD)
venv\Scripts\activate  
# En Windows (PowerShell)
venv\Scripts\Activate.ps1  
# En macOS/Linux
source venv/bin/activate  
# Instalar Django y DRF
pip install django djangorestframework  
# Crear el proyecto Django
django-admin startproject gestion  
# Entrar al proyecto
cd gestion  
# Crear una aplicación dentro del proyecto
python manage.py startapp api  
# Aplicar migraciones iniciales
python manage.py migrate  
# Crear un superusuario para el panel de administración
python manage.py createsuperuser  
# Después de definir modelos en models.py
python manage.py makemigrations
python manage.py migrate 
#Luego, abrir el navegador en: http://127.0.0.1:8000/
python manage.py runserver  
# Inicializar Git en el proyecto
git init  

# Agregar un repositorio remoto (cambiar con tu URL)
git remote add origin https://github.com/TU-USUARIO/gestion-educativa.git  

# Crear archivo .gitignore (para ignorar archivos innecesarios)
echo "venv/" >> .gitignore  
echo "__pycache__/" >> .gitignore  
echo "db.sqlite3" >> .gitignore  

# Agregar archivos al repositorio
git add .  

# Hacer un commit
git commit -m "Primer commit - Proyecto Django"  

# Subir el código a GitHub
git push -u origin main  
# Mover el archivo PDF a la carpeta raíz del proyecto

# Agregarlo al repositorio
git add analisis_y_diagrama.pdf  

# Hacer un commit con el PDF
git commit -m "Añadiendo PDF con análisis y diagrama"  

# Subir los cambios a GitHub
git push origin main  
git pull origin main --rebase  
git push -f origin main  

#desactivar 
deactivate



