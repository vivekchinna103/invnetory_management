from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        self.fields['description'].required =False
        self.fields['Factory_name'].empty_label="Select"