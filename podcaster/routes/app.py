from django.urls import path
import podcaster.views.app as app

from podcaster.constant import ROOT
app_name = "app"

urlpatterns = [
    path('dashboard/', app.dashboard, name="dashboard"),
    path('login/', app.login, name='login'),
    path('register/', app.register, name='register'),
    path('search/', app.search, name='search'),
]