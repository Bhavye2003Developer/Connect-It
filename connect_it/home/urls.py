from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("enter/", enter, name="enter"),
    path("up/", up, name="up"),
    path("down/", down, name="down"),
    path("left/", left, name="left"),
    path("right/", right, name="right"),
    path("scrollUp/", ScrollUp, name="scrollUp"),
    path("scrollDown/", ScrollDown, name="scrollDown"),
    path("write", write, name="write")
]
