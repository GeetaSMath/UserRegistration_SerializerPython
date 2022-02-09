from django.urls import path, re_path
from .views import Register, Login

urlpatterns = [
    path('register', Register.as_view(), name='register'),
    re_path(r'^register/(?P<username>[\w0-9-]+)/$',Register.as_view(),name='register'),
    path('login', Login.as_view(), name='login'),
]