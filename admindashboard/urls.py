from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="admin-dashboard.index"),
    path('users', views.users, name="admin-dashboard.users"),
    path('residents', views.residents, name="admin-dashboard.residents"),
    path('logs', views.logs, name="admin-dashboard.logs"),
]
