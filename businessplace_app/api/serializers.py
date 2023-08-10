from rest_framework import serializers

from businessplace_app.models import BusinessPlace, RatingAndComment

class BusinessPlaceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BusinessPlace
        fields = "__all__"

class RatingAndCommentSerializer(serializers.ModelSerializer):
    
    placeRac = BusinessPlaceSerializer(read_only=True)
    
    class Meta:
        model = RatingAndComment
        fields = "__all__"
