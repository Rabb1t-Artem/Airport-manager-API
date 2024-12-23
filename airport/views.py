from rest_framework.viewsets import ModelViewSet

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


class AirportViewSet(ModelViewSet):
    model = Airport
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class RouteViewSet(ModelViewSet):
    model = Route
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class CrewViewSet(ModelViewSet):
    model = Crew
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class AirplaneTypeViewSet(ModelViewSet):
    model = AirplaneType
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class AirplaneViewSet(ModelViewSet):
    model = Airplane
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class FlightViewSet(ModelViewSet):
    model = Flight
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class OrderViewSet(ModelViewSet):
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TicketViewSet(ModelViewSet):
    model = Ticket
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
