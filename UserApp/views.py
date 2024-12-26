from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def UserCreateApi(request):
    """
    Create a new user.
    """
    # Extract data from request
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    # Check if all required fields are provided
    if not username or not email or not password:
        return Response({'error': 'Username, email, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Create a new user instance
        User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'User  created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def UserLoginApi(request):
    """
    Log in a user.
    """
    username = request.data.get('username')  # Use request.data instead of request.POST
    password = request.data.get('password')  # Use request.data instead of request.POST

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)  # Log the user in
        return Response({'message': 'User  logged in successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)  # Return error for failed login
@api_view(['GET'])
def ProtectedUsersApi(request):
    """
    The function `ProtectedUsersApi` checks if the user is authenticated and returns a message
    accordingly.

    :param request: The `request` parameter in the `ProtectedUsersApi` function is typically an object
    that contains information about the incoming HTTP request, such as the user making the request, the
    request method (GET, POST, etc.), request headers, request data, and other relevant information. In
    this context, it
    :return: The `ProtectedUsersApi` function is returning a response based on the authentication status
    of the user making the request. If the user is authenticated, it returns a JSON response with a
    message saying "Hello, authenticated user!" and a status code of 200 (OK). If the user is not
    authenticated, it returns a JSON response with an error message saying "You are not authenticated"
    and a status
    """
    if request.user.is_authenticated:
        return Response({'message': 'Hello, authenticated user!'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)