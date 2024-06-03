# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     
    path('harga/', views.harga_list, name='harga_list'),
    path('harga/create/', views.harga_create, name='harga_create'),
    path('harga/update/<int:pk>/', views.harga_update, name='harga_update'),
    path('harga/delete/<int:pk>/', views.harga_delete, name='harga_delete'),

    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    path('countries/', views.country_list, name='country_list'),
    path('countries/create/', views.country_create, name='country_create'),
    path('countries/<int:pk>/edit/', views.country_update, name='country_update'),
    path('countries/<int:pk>/delete/', views.country_delete, name='country_delete'),

    path('pos/', views.pos_list, name='pos_list'),
    path('pos/create/', views.pos_create, name='pos_create'),
    path('pos/update/<int:pk>/', views.pos_update, name='pos_update'),
    path('pos/delete/<int:pk>/', views.pos_delete, name='pos_delete'),

    path('prediksi/create/', views.prediksi_create, name='prediksi_create'),
    

]

