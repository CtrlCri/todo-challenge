from django.urls import path

from users import views


urlpatterns = [
    path('list/', views.ListUserView.as_view()),
]