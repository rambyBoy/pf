from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.index, name='index'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('crear/', views.crear, name='crear'),
    path('categorias/', views.cats, name="categorias"),
    path('catdelete/<int:id>', views.catdelete, name='catdelete'),
    path('crearcat/', views.crearcat, name='crearcat'),
    path('catedit/<int:id>', views.catedit, name='catedit'),
    path('comprar/<int:id>', views.comprar, name="comprar"),
    path('error/', views.error, name="error")
]