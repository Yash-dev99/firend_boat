from django.urls import path

from . import views

urlpatterns = [
    path("<user_name>", views.user_page,name='user_page'  ),
]