from django.forms import ModelForm
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import  Order,Customer, Product, Category,Collection,Tag

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        
class OrderForm (ModelForm):
    class Meta :
        model = Order
        fields = '__all__'
        
class ProductForm (ModelForm):
    class Meta :
        model = Product
        fields = '__all__'

class CollectionForm (ModelForm):
    class Meta :
        model = Collection
        fields = '__all__'

class CategoryForm (ModelForm):
    class Meta :
        model = Category
        fields = '__all__'               

class TagForm (ModelForm):
    class Meta :
        model = Tag
        fields = '__all__'       
        
class CreateUserForm(UserCreationForm):
    class  Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']