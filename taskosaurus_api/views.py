"""
File for rendering root route in the Taskosaurus API.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
)


@api_view((['POST']))
def logout_route(request):
    """
    Route that fixes the logout bug
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,

    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
    )
    return response


@api_view()
def root_route(request):
    """
    Function which displays welcome message to user on
    the root route.
    """
    return Response({
        "message": "Welcome to the Taskosaurus API!"
    })
