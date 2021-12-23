from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Ship, ShipClass, Feature, TransferRequest
from .serializers import ShipClassSerializer, ShipSerializer, FeatureSerializer, TransferRequestSerializer, UserSerializer
from rest_framework import status
from .permissions import IsCaptain, IsAdmiral
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.

# Admiral views

def get_ship_object(pk):
    try:
        return Ship.objects.get(pk=pk)
    except:
        raise Http404

def get_user_object(pk):
    try:
        return User.objects.get(pk=pk)
    except:
        raise Http404

@api_view(['POST'])
@permission_classes([IsAdmiral])
def add_new_ship(request):
    serializer = ShipSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAdmiral])
def get_transfer_requests(request):
    all_requests = TransferRequest.objects.all()
    serializer = TransferRequestSerializer(all_requests, many=True)
    return Response(serializer)

@api_view(['PATCH'])
@permission_classes([IsAdmiral])
def approve_transfer_request(request):
    # switch user to requested ship
    pass


# Captain views
# see whole crew of any ship
# add new feature to own ship if engineer is assigned

@api_view(['GET'])
@permission_classes([IsCaptain])
def get_ship_crew(request, ship_id):
    ship_crew = User.objects.filter(ship__id=ship_id)
    serializer = UserSerializer(ship_crew, many=True)
    return Response(serializer.data)


# User views
# see whole crew of own ship
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_own_crew(request, ship_id):
    ship_crew = User.objects.filter(ship__id=ship_id)
    serializer = UserSerializer(ship_crew)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_transfer_request(request, ship_id):
    new_transfer = TransferRequest(user=request.user, ship=ship_id)
    