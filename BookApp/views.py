from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BookModel
from .serializers import BookSerializer  # Assuming a serializer is created for BookModel
from rest_framework.viewsets import ModelViewSet
# @api_view(['GET'])
# def BookListApi(request):
#     """
#     Retrieve a list of all books.
#     """
#     books = BookModel.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def BookCreateApi(request):
#     """
#     Create a new book.
#     """
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         book = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def BookUpdateApi(request, id):
#     """
#     Update an existing book by ID.
#     """
#     try:
#         book = BookModel.objects.get(id=id)
#     except BookModel.DoesNotExist:
#         return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

#     serializer = BookSerializer(book, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def BookDeleteApi(request, id):
#     """
#     Delete a book by ID.
#     """
#     try:
#         book = BookModel.objects.get(id=id)
#         book.delete()
#         return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#     except BookModel.DoesNotExist:
#         return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)


class BookViewSet(ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new book and return a success message.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {'message': 'Book created successfully', 'data': serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        """
        Update an existing book and return a success message.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(
            {'message': 'Book updated successfully', 'data': serializer.data},
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        """
        Delete a book and return a success message.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Book deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )