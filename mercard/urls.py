"""mercard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from pages.views import home_view
from products.views import product_det_view, product_forms_view, SearchPage
from accounts.views import login_page, logout_view, register_page, registerstaff_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name= 'home'),
    path('product/', product_det_view),
    path('create/', product_forms_view),
    path('login/', login_page),
    path('register/', register_page),
    path('logout/', logout_view),
    path('registerseller/', registerstaff_view),
    path('search/', SearchPage, name='search_result'),
]
