from django.urls import path
from . import views
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    path('appointment', views.meeting, name='appointment'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('new_app', views.new_app, name='new_app'),
]
