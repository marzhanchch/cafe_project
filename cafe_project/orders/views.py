from django.views.generic import TemplateView, FormView, DeleteView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django import forms
from django.db import models
from django.utils.safestring import mark_safe
from django import template
from .models import Customer, MenuItem, Order
from .forms import CustomerForm, MenuItemForm, OrderForm



class CustomerListView(TemplateView):
    template_name = "orders/customer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context

class CustomerFormView(FormView):
    template_name = "orders/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')
    template_name = "orders/customer_confirm_delete.html"

class MenuListView(TemplateView):
    template_name = "orders/menu_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.all()
        return context

class MenuItemFormView(FormView):
    template_name = "orders/menu_form.html"
    form_class = MenuItemForm
    success_url = reverse_lazy('menu_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class MenuDeleteView(DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menu_list')
    template_name = "orders/menu_confirm_delete.html"

class OrderListView(TemplateView):
    template_name = "orders/order_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        return context

class OrderFormView(FormView):
    template_name = "orders/order_form.html"
    form_class = OrderForm
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        order = form.save()
        order.calculate_total_price()
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
    template_name = "orders/order_confirm_delete.html"



register = template.Library()

@register.filter(name='status_color')
def status_color(value):
    colors = {"Ожидается": "yellow", "В процессе": "blue", "Завершён": "green"}
    return mark_safe(f'<span style="color: {colors.get(value, "black")};">{value}</span>')

@register.simple_tag
def menu_by_category(category):
    items = MenuItem.objects.filter(category=category)
    return items


urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list"),
    path("customers/add/", CustomerFormView.as_view(), name="customer_add"),
    path("customers/edit/<int:pk>/", CustomerFormView.as_view(), name="customer_edit"),
    path("customers/delete/<int:pk>/", CustomerDeleteView.as_view(), name="customer_delete"),
    path("menu/", MenuListView.as_view(), name="menu_list"),
    path("menu/add/", MenuItemFormView.as_view(), name="menu_add"),
    path("menu/edit/<int:pk>/", MenuItemFormView.as_view(), name="menu_edit"),
    path("menu/delete/<int:pk>/", MenuDeleteView.as_view(), name="menu_delete"),
    path("orders/", OrderListView.as_view(), name="order_list"),
    path("orders/add/", OrderFormView.as_view(), name="order_add"),
    path("orders/edit/<int:pk>/", OrderFormView.as_view(), name="order_edit"),
    path("orders/delete/<int:pk>/", OrderDeleteView.as_view(), name="order_delete"),
    path("orders/status/<str:status>/", OrderListView.as_view(), name="orders_by_status"),
    path("menu-items/category/<str:category>/", OrderListView.as_view(), name="menu_by_category"),
]
