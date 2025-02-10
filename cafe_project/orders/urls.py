from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/edit/<int:id>/', views.customer_edit, name='customer_edit'),
    path('customers/delete/<int:id>/', views.customer_delete, name='customer_delete'),

    path('menu-items/', views.menu_list, name='menu_list'),
    path('menu-items/add/', views.menu_add, name='menu_add'),
    path('menu-items/edit/<int:id>/', views.menu_edit, name='menu_edit'),
    path('menu-items/delete/<int:id>/', views.menu_delete, name='menu_delete'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.order_add, name='order_add'),
    path('orders/edit/<int:id>/', views.order_edit, name='order_edit'),
    path('orders/delete/<int:id>/', views.order_delete, name='order_delete'),
]
