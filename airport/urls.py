from rest_framework import routers
from django.urls import path, include
from .views import (
    AirplaneViewset,
    RouteViewset,
    CrewViewSet,
    AirplaneTypeViewSet,
    AirplaneViewSet,
    FlightViewset,
    OrderViewSet,
    TicketViewSet
)

router = routers.DefaultRouter()

router.register("airplanes", AirplaneViewset)
router.register("routes", RouteViewset)
router.register("crews", CrewViewSet)
router.register("airplane-types", AirplaneTypeViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("flights", FlightViewset)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
]