"""jal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage, name = 'Home'),
    path('opform/',views.OpForm,name = 'OpForm'),
    path('logout/',views.logout_view, name = 'Log_out'),
    path('locations/',views.locations_view,name = 'locations'),
    path('sub_location/',views.sub_location_details_view,name = 'sub_locations'),
    path('equipments/',views.equipment_view,name = 'equipments'),
    path('changepassword/',views.ChangePassword, name = 'changepassword'),
    path('equipmentlocation/',views.EquipmentLocation,name = 'equipmentlocation'),
    path('equipmenttype/',views.EquipmentType,name = 'equipmenttype'),
    path('accountdetails/',views.AccountDetails,name = 'accountdetails'),
    path('map/',views.MapView,name = 'map')
]

