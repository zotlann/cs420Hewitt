from django.urls import path
from . import views

urlpatterns = [
        path('',views.Login, name='login'),
        path('home/',views.Home, name='home'),
        path('create-account/',views.CreateAccount, name='create-account'),
        path('all-recipes/',views.Recipes,name='recipes'),
        path('recipes/chicken-parmesan',views.Chicken,name='chicken'),
        path('logout/',views.Logout,name='logout'),
]
