from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="booksindex"),
    path('storedetails',views.StoreDetails,name="storeditals"),
    path('showbooks',views.ShowBooks,name="showbooks")
]