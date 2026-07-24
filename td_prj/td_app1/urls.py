from django.urls import path
from .import views
urlpatterns = [
    path('',views.td_views),
    path('del/<int:id>',views.td_del,name='del')
]
