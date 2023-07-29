from django.urls import path
from house import views

urlpatterns =[
    path("", views.cites, name="cites"),
    path("cite/<str:pk>", views.singlecite, name="singlecite"),
    path("addcite", views.addcite, name="addcite"),
    path("update/<str:pk>", views.updatecite, name="updatecite"),
    path("delete/<str:pk>", views.deletecite, name="deletecite"),
    path("selecttype/", views.selecttype, name="selecttype"),
]