from rest_framework import serializers
from .models import FoodType, Food, Comment, Review
from django.contrib.auth.models import User


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ('id', 'name')

class FoodSerializer(serializers.ModelSerializer):
    food_type = FoodTypeSerializer()
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )
    class Meta:
        model = Food
        fields = ('id', 'name','price', 'food_type', 'content', 'comments')
        

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Comment
        fields = ('id', 'author', 'food', 'created_at','text')
        read_only_fields = ('created_at',)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()
        return user




class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    food = serializers.ReadOnlyField(source='food.name')
    class Meta:
        model = Review
        fields = ('id', 'author', 'food', 'rating', 'text', 'created_at')