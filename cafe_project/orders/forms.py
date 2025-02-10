from django import forms
from .models import Customer, MenuItem, Order, OrderItem

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone_number']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'category', 'available']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'status']

    items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    quantities = forms.CharField(max_length=255, required=False, help_text="Enter quantities separated by commas")

    def save(self, commit=True):
        order = super().save(commit=False)
        if commit:
            order.save()

        items = self.cleaned_data['items']
        quantities = self.cleaned_data['quantities'].split(',') if self.cleaned_data['quantities'] else []

        if len(items) != len(quantities):
            raise forms.ValidationError("Количество позиций и количеств не совпадает.")

        for item, quantity in zip(items, quantities):
            order_item = OrderItem(order=order, menu_item=item, quantity=int(quantity))
            order_item.save()

        order.calculate_total_price()
        return order

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'menu_item', 'quantity']


