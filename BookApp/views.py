from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import BookModel
from .serializers import BookSerializer
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 2  # Number of items per page
    page_size_query_param = 'page_size'  # Allows client to override the page size
    max_page_size = 100  # Maximum limit for page size

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is logged in for all actions
    pagination_class = CustomPagination  # Use the custom pagination class

    def get_queryset(self):
        """
        Override the queryset to return only books belonging to the logged-in user.
        """
        return BookModel.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        """
        Override the create method to set the logged-in user as the author of the book.
        """
        serializer.save(author=self.request.user)

    def check_ownership(self, instance):
        """
        Centralized method to check if the logged-in user is the creator of the book.
        """
        if instance.author != self.request.user:
            return Response(
                {'error': 'You do not have permission to perform this action.'},
                status=status.HTTP_403_FORBIDDEN
            )
        return None

    def perform_update(self, serializer):
        """
        Override the update method to ensure only the creator of the book can update it.
        """
        instance = self.get_object()
        ownership_check = self.check_ownership(instance)
        if ownership_check:
            return ownership_check
        serializer.save()

    def perform_destroy(self, instance):
        """
        Override the destroy method to ensure only the creator of the book can delete it.
        """
        ownership_check = self.check_ownership(instance)
        if ownership_check:
            return ownership_check
        instance.delete()