from django.urls import path


from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dash_board', views.dash_board, name='dash_board'),
]
