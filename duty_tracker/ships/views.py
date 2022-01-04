from django.http.response import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from .models import Ship, ShipClass, Feature, TransferRequest
from .serializers import ShipClassSerializer, ShipSerializer, FeatureSerializer, TransferRequestSerializer, UserSerializer
from rest_framework import status
from .permissions import IsCaptain, IsAdmiral, ShipHasEngineer
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
    
def get_transfer_object(pk):
    try:
        return TransferRequest.objects.get(pk)
    except:
        raise Http404

def get_or_create_feature(feature_name):
    try:
        return Feature.objects.get(name=feature_name)
    except:
        new_feature = Feature(name=feature_name)
        new_feature.save()
        return new_feature

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
def approve_transfer_request(request, transfer_id):
    transfer_to_approve = get_transfer_object(transfer_id)
    requesting_crewman = transfer_to_approve.user
    requesting_crewman.ship = transfer_to_approve.ship
    requesting_crewman.save()
    return Response(status=status.HTTP_200_OK)
    

# Captain views
# see whole crew of any ship
# add new feature to own ship if engineer is assigned

@api_view(['GET'])
@permission_classes([IsCaptain])
def get_ship_crew(request, ship_id):
    ship_crew = User.objects.filter(ship__id=ship_id)
    serializer = UserSerializer(ship_crew, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsCaptain, ShipHasEngineer])
def add_feature(request, feature_name):
    feature_to_add = get_or_create_feature(feature_name)
    captains_ship = get_ship_object(request.user.ship.id)
    captains_ship.features.add(feature_to_add)
    return Response(status=status.HTTP_201_CREATED)


# User views
# see whole crew of own ship
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_own_crew(request):
    ship_crew = User.objects.filter(ship__id=request.user.ship.id)
    serializer = UserSerializer(ship_crew, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_transfer_request(request, ship_id):
    new_transfer = TransferRequest(user=request.user, ship=ship_id)
    new_transfer.save()
    return Response(status=status.HTTP_201_CREATED)

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_test(request):
    ship = request.user.ship
    for item in ship.user_set.all():
        print(item)
    if ship.user_set.filter(position="CPT").exists():
        print(request.user)
