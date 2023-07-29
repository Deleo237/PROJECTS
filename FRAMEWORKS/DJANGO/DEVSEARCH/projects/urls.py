from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>', views.singleproject, name='singleproject'),
    path('createproject', views.createproject, name='createproject'),
    path('updateproject/<int:pin>/<str:pk>', views.updateproject, name='updateproject'),
    path('deleteproject/<int:pin>/<str:pk>', views.deleteproject, name='deleteproject'),
    path('test', views.test, name='test')
]
