from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "index"),
    path("post/<slug:slug>",views.detail,name = "detail"),
    path("new_url",views.new_url_view,name = "new_url"),
    path("old_url",views.old_url_redirect,name = "old_url"),
    path("contact",views.contact_view,name="contact"),
    path("about",views.about_view,name="about")
]