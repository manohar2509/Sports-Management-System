from django.urls import path
from . import views
app_name = 'basic_app'
urlpatterns = [
 path('register',views.register,name = 'register'),
 path('user_login/',views.user_login,name = 'user_login'),
 path('athlete_list/',views.AthleteListView.as_view(),name = "list"),
 path('athlete_list/<int:pk>/',views.AthleteDetailView.as_view(),name = "detail"),
 path('result_men/',views.ResultMenListView.as_view(),name = "result_men"),
 path('result_women/',views.ResultWomenListView.as_view(),name = "result_women"),
  path('medals/',views.MedalsListView.as_view(),name = "medals"),
]
