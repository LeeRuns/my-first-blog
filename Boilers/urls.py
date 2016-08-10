from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.Boilerview,name='Boilerview'), #set based on the name ofthe view we want to call
]
