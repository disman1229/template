from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('',views.index),
    path('students/',views.students),
    path('good/<int:id>/',views.good,name='good'),
    path('main/',views.main),
    path('detail/',views.detail),
    path('verifycode/',views.verifycode),
    path('verifycodefile/',views.verifycodefile),
    path('verifycodecheck/',views.verifycodecheck)
]