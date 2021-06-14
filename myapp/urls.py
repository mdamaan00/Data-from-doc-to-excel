from django.urls import path
from .views import *

urlpatterns = [
    path('', my_view, name='my-view'),
    path('pdfview/<int:pkid>/', pdfview, name='pdfview')
]
