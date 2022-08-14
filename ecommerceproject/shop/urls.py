
from django.urls import path, include
from . import views
app_name='shop'
urlpatterns = [
    path('', views.allprodcat, name='allprodcat'),
    path('<slug:c_slug>/', views.allprodcat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodetail, name='procatdetail'),
]