from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('', views.Management.as_view(), name='management'),
    path('passwordChange/', views.PasswordChange.as_view(), name='passwordChange'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'),
    path('userdelete/<int:userid>', views.UserDelete.as_view(), name='userDelete'),
    path('add/', views.AddService.as_view(), name='addService'),
    path('detail/<int:serviceid>', views.Detail.as_view(), name='detail'),
    path('update/<int:serviceid>', views.Update.as_view(), name='update'),
    path('delete/<int:serviceid>', views.Delete.as_view(), name='delete'),
]