from rest_framework.permissions import BasePermission
from .models import User


class BranchCheck(BasePermission):
    def has_object_permission(self, request, view, obj):
        branch = int(User.objects.get(username=request.user).branch)
        return obj.branchCode == branch
