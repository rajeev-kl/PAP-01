# django imports
from django.urls import include, path

# external imports
from rest_framework import routers

# local imports
from .views import CountryView, UserView

router = routers.SimpleRouter()
router.register(r"country", CountryView)
router.register(r"user", UserView)

urlpatterns = [path("", include(router.urls))]
