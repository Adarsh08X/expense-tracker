
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home , name="home"),
    path('bills/', bills , name="bills"),
    path('past-expenditure/', past_expenditure , name="past_expenditure"),
    path('profile/', profile , name="profile"),
    path('payment/', payment , name="payment"),
   
]
