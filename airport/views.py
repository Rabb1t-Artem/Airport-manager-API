from datetime import datetime   # noqa

from django.db.models import F, Count   # noqa
from drf_spectacular.types import OpenApiTypes   # noqa
from drf_spectacular.utils import extend_schema, OpenApiParameter   # noqa
from rest_framework import viewsets, mixins, status   # noqa
from rest_framework.decorators import action   # noqa
from rest_framework.pagination import PageNumberPagination   # noqa
from rest_framework.permissions import IsAuthenticated, IsAdminUser   # noqa
from rest_framework.response import Response   # noqa
from rest_framework.viewsets import GenericViewSet

from airport.models import (
    Airport,
    Route,
    Crew,
    AirplaneType,
    Airplane,
    Flight,
    Order,
    Ticket,
)
from airport.serializers import (
    AirportSerializer,
    RouteSerializer,
    RouteListSerializer,
    CrewSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer,
    AirplaneListSerializer,
    FlightSerializer,
    FlightListSerializer,
    FlightDetailSerializer,
    OrderSerializer,
    OrderListSerializer,
    TicketSerializer,
)


class AirportViewSet(viewsets.ModelViewSet):
    model = Airport
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class RouteViewSet(viewsets.ModelViewSet):
    model = Route
    queryset = Route.objects.select_related("source", "destination").all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return RouteListSerializer
        return RouteSerializer


class CrewViewSet(viewsets.ModelViewSet):
    model = Crew
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    model = AirplaneType
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    model = Airplane
    queryset = Airplane.objects.select_related("airplane_type").all()
    
    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneListSerializer
        return AirplaneSerializer


class FlightViewSet(viewsets.ModelViewSet):
    model = Flight
    queryset = (
        Flight.objects.select_related("route", "airplane")
        .prefetch_related("crew")
        .all()
    )
    
    def get_serializer_class(self):
        if self.action == "list":
            return FlightListSerializer
        if self.action == "retrieve":
            return FlightDetailSerializer
        return FlightSerializer


class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.prefetch_related(
        "tickets__flight__route",
        "tickets__flight__airplane__name",
    )
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer
        return OrderSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    model = Ticket
    queryset = (
        Ticket.objects.select_related("flight", "order")
        .prefetch_related(
            "flight__route",
            "flight__airplane",
            "flight__crew"
        )
        .all()
    )
    serializer_class = TicketSerializer
