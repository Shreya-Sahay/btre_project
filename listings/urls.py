from django.urls import path
# if you want to define path then you need to bring that packagr in

# from all
from . import views

urlpatterns = [
    #path we want is nothing(home page) so 1st parameter empty
    #2nd  method connect to view and method to be called is index
    #3rd name to easily acces path called index
    #for listing/23 i.e is

    path('',views.index, name='listings'),
    path('<int:listing_id>',views.listing, name='listing'),
    path('search',views.search, name='search'),
]