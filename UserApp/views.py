from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
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
@csrf_exempt  # Consider the security implications of this decorator
def UserLoginApi(request):
    """
    Log in a user and return JWT tokens.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def ProtectedUsersApi(request):
    """
    A protected API endpoint that requires authentication.
    """
    if request.user.is_authenticated:
        return Response({'message': 'Hello, authenticated user!',
                         'username': request.user.username}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)