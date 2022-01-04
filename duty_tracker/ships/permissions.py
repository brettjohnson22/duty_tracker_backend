from rest_framework import permissions



class IsCaptain(permissions.BasePermission):
    message = 'You are not a Captain'

    def has_permission(self, request, view):
        user = request.user
        if user.rank == "CPT" or user.rank == "ADM":
            return True
    
class IsAdmiral(permissions.BasePermission):
    message = 'You are not an Admiral'

    def has_permission(self, request, view):
        user = request.user
        if user.rank == "ADM":
            return True

class ShipHasEngineer(permissions.BasePermission):
    message = 'Your ship does not have an Engineer'

    def has_permission(self, request, view):
        ship = request.user.ship
        if ship.user_set.filter(position="ENG").exists():
            return True 