"""CCENTDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CCENTDjango.views import inicio, quienes_somos, cursos, av, autom, EAD, pcylap, materiales, robotica, servicios,faq
from document.views import editor, delete_document

urlpatterns = [
    path('', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('quienes_somos/',quienes_somos),

    path('cursos/',cursos),
    path('av/',av),
    path('EAD/', EAD),
    path('pcylap/',pcylap),
    path('autom/', autom),
    path('robotica/', robotica),
    
    path('materiales/', materiales),
    path('servicios/',servicios),
    path('faq/',faq)
    
]
