from . import views
from django.urls import path, include
app_name='ecommerceapp'

urlpatterns = [
    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/',views.AllProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='ProdCatDetail'),
]