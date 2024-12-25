from rest_framework import serializers
from .models import BookModel

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookModel to handle serialization and validation.
    """

    class Meta:
        model = BookModel
        fields = ['id', 'title', 'author', 'price', 'publication_date']
        read_only_fields = ['id']  # ID should be read-only as it is auto-generated

    def validate_price(self, value):
        """
        Validate that the price is a positive number.
        """
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate_publication_date(self, value):
        """
        Validate that the publication date is not in the future.
        """
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value