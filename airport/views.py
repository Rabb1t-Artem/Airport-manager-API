from rest_framework.viewsets import ViewSet

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
    CrewSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer,
    FlightSerializer,
    OrderSerializer,
    TicketSerializer,
)


class AirportViewSet(ViewSet):
    model = Airport
    serializer_class = AirportSerializer


class RouteViewSet(ViewSet):
    model = Route
    serializer_class = RouteSerializer


class CrewViewSet(ViewSet):
    model = Crew
    serializer_class = CrewSerializer


class AirplaneTypeViewSet(ViewSet):
    model = AirplaneType
    serializer_class = AirplaneTypeSerializer


class AirplaneViewSet(ViewSet):
    model = Airplane
    serializer_class = AirplaneSerializer


class FlightViewSet(ViewSet):
    model = Flight
    serializer_class = FlightSerializer


class OrderViewSet(ViewSet):
    model = Order
    serializer_class = OrderSerializer


class TicketViewSet(ViewSet):
    model = Ticket
    serializer_class = TicketSerializer
