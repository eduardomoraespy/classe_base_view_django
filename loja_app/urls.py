from django.urls import path

app_name = 'loja_app'

from loja_app import views

urlpatterns = [
    path('cliente/', views.ClienteList.as_view(), name='cliente'),
    path('cliente/cadastro/', views.ClienteCreate.as_view(), name='create_cliente'),
    path('cliente/editar/<int:pk>/', views.ClienteUpdate.as_view(), name='edit_cliente'),
    path('cliente/detail/<int:pk>/', views.ClienteDetail.as_view(), name='detail_cliente'),
    path('cliente/delete/<int:pk>/', views.ClienteDelete.as_view(), name='delete_cliente'),
]