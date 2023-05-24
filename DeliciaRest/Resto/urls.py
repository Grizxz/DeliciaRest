from django.urls import path
from .views import*
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path('',index,name=""),
    #Configuración del Login
    path('login/',login, name="login"),
    path('login',LoginView.as_view(template_name='registration/login.html'),name="login"),
    path('logout',LogoutView.as_view(template_name='app/index.html'),name="logout"),
    #Configuración de Registro
    path('register', register, name="agregarUsuario")
]
