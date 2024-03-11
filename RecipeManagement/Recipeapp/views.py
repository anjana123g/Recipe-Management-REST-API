from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, ListAPIView
from Recipeapp.models import Recipe
from Recipeapp.serializers import RecipeSerializer,ReviewSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Recipeapp.models import Review

# Create your views here.
# def home(request):
#     return render(request,'home.html')

class RecipeCreate(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeList(ListAPIView):
    serializer_class = RecipeSerializer
    queryset=Recipe.objects.all()

class Detail(APIView):
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe_instance = self.get_object(pk)
        serializer = RecipeSerializer(recipe_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        recipe_instance = self.get_object(pk)
        serializer = RecipeSerializer(recipe_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe_instance = self.get_object(pk)
        recipe_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ReviewCreate(APIView):
#     # permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)  # Associate the review with the current user
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ReviewCreate(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class Review(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except :
            raise Http404

    def get(self, request, pk):
        review_instance = self.get_object(pk)
        serializer = ReviewSerializer(review_instance)
        return Response(serializer.data)

    def put(self, request, pk):
        review_instance = self.get_object(pk)
        serializer = ReviewSerializer(review_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review_instance = self.get_object(pk)
        review_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Search(APIView):
    def get(self, request):
        query= self.request.query_params.get('search')
        if (query):
            recipe=Recipe.objects.filter(Q(recipe_name__icontains=query) | Q(ingredients__icontains=query))
            r=RecipeSerializer(recipe,many=True)
            return Response(r.data)

class RecipeFilter(APIView):
    def get(self, request):
        query= self.request.query_params.get('recipetype')
        if (query):
            recipe = Recipe.objects.filter(Q(instructions__icontains=query) | Q(ingredients__icontains=query) | Q(meal_type__icontains=query))
            r = RecipeSerializer(recipe, many=True)
            return Response(r.data)
        else:
            return Response({'detail': 'No search query provided'})