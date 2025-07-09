from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('users/', include('users.urls')),  # rotas: /users/register, /users/login, /users/logout
    path('tasks/', include('tasks.urls')),  # rotas: /tasks/...
]
