from shop import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('shop/<int:id>',views.quickview,name='quickview')
]
