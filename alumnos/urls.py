from django.urls import path
from . import views

urlpatterns = [    
    path('index', views.index , name="index"),

    path('crud', views.crud, name="crud"),
    path('alumnosAdd', views.alumnosAdd,name="alumnosAdd"),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),

    path('crud_genero', views.crud_genero, name="crud_genero"),
    path('generosAdd', views.generosAdd,name="generosAdd"),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_Edit/<str:pk>', views.generos_Edit, name='generos_Edit'),

]