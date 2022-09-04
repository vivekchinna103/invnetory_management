from django.urls import path
from . import views


urlpatterns=[
    path('',views.product_form, name="product _insert" ),  #get and post req for insert operation
    path('<int:id>/',views.product_form,name='product_update'), #get and post req for update operation
    path('list/',views.product_list,name='product_list') , #get req to retrieve and dispaly details
    path('delete/<int:id>/',views.product_delete,name='product_delete')
]