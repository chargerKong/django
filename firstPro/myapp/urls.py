from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^app$', views.index,name="page1"),
    url(r'^app1/(2018)',views.func1,name="page2"),
    url(r'^app2/([0-9]{4})',views.func1),
    url(r'^app3/([0-9]{4})/([a-zA-Z]+)',views.func2),
]