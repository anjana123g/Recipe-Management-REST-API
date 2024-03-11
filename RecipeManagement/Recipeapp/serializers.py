from django.contrib.auth.models import User
from rest_framework import serializers

from Recipeapp.models import Recipe,Review



class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields=('recipe_name','ingredients','instructions','cuisine','meal_type')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']

    def create(self, validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u