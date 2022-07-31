"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

# user/tests/test_user_api.py 12行目 CREATE_USER_URL = reverse('user:create')
#  逆引き参照に使用。
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]