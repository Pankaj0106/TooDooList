from django.urls import path
from newapp import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('create/',views.CreateListView.as_view(),name='create'),
    path('update/<int:pk>/',views.UpdateListView.as_view(),name='update'),
    path('delete/<int:pk>/',views.DeleteListView.as_view(),name='delete')
]