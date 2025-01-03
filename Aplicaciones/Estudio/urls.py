#URLS especificas de la aplicacion
from django.urls import path

from.import views
urlpatterns = [

    path('',views.inicio),
    path('inicio/', views.inicio),
    path('nuevousuario/',views.nuevousuario),
    path('listadousuario/',views.listadousuario),
    path('guardarusuario/',views.guardarusuario),
    path('eliminarusuario/<int:id>',views.eliminarusuario),
    path('editarusuario/<int:id>',views.editarusuario),
    path('procesareditarusuario/', views.procesareditarusuario),  
 

    path('nuevohabito/', views.nuevohabito),
    path('listadohabito/', views.listadohabito),
    path('guardarhabito/', views.guardarhabito),
    path('eliminarhabito/<int:id>', views.eliminarhabito),
    path('editarhabito/<int:id>', views.editarhabito),
    path('procesareditarhabito/', views.procesareditarhabito),
  


    path('listadoprogreso/', views.listadoprogreso),
    path('guardarprogreso/', views.guardarprogreso),
    path('eliminarprogreso/<int:id>', views.eliminarprogreso),
    path('editarprogreso/<int:id>', views.editarprogreso),
    path('procesareditarprogreso/', views.procesareditarprogreso),




    path('nuevanotificacion/', views.nuevanotificacion),
    path('listadonotificacion/', views.listadonotificacion),
    path('guardarnotificacion/', views.guardarnotificacion),
    path('eliminarnotificacion/<int:id>', views.eliminarnotificacion),
    path('editarnotificacion/<int:id>', views.editarnotificacion),
    path('procesareditarnotificacion/', views.procesareditarnotificacion),




    path('nuevaficha/', views.nuevaficha),
    path('listadometa/', views.listadometa),
    path('guardarmeta/', views.guardarmeta),
    path('eliminarmeta/<int:id>', views.eliminarmeta),
    path('editarmeta/<int:id>', views.editarmeta),
    path('procesareditarmeta/', views.procesareditarmeta),



]


