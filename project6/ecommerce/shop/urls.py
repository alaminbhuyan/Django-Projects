from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = "shop"),
    path("about/",views.about, name = "AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/",views.tracker, name = "TrakingStatus"),
    path("search/",views.search, name = "Search"),
    path("productview/",views.productview, name = "ProductView"),
    path("chacker/",views.chacker, name = "Chacker"),
]
