from django.urls import path
from port.views import PortDV, PortLV

app_name = 'port'
urlpatterns = [
    path('', PortLV.as_view(), name='index'),
    path('<int:pk>/', PortDV.as_view(), name='detail'),
]


    #path('port/', PortLV.as_view(), name='index'),
    #path('port/<int:pk>/', PortDV.as_view(), name='detail'),