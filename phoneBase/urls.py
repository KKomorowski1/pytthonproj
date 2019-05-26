from django.urls import path

from . import views

app_name = 'phoneBase'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.phone_save, name='add_phone'),
    path('delete/<int:pk>', views.PhoneDelete.as_view(), name='phone_delete'),
    path('update/<int:pk>', views.PhoneUpdate.as_view(), name='phone_update'),
    path('<int:pk>/updateDetail', views.DetailsUpdate.as_view(), name='details_update'),

]
