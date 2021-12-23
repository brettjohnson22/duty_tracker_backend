from rest_framework import permissions



class IsCaptain(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.rank == "CPT" or user.rank == "ADM":
            return True
    
class IsAdmiral(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.rank == "ADM":
            return True