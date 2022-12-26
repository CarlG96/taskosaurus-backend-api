"""
File for rendering root route in the Taskosaurus API.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    """
    Function which displays welcome message to user on
    the root route.
    """
    return Response({
        "message": "Welcome to the Taskosaurus API!"
    })
