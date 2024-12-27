from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

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

        token,created = Token.objects.get_or_create(user=user)
        return Response({'message': 'User  logged in successfully',
                         'token':token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)  # Return error for failed login
@api_view(['GET'])
def ProtectedUsersApi(request):
    if request.user.is_authenticated:
        return Response({'message': 'Hello, authenticated user!',
                         'username': request.user.username}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)