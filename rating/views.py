from rest_framework.decorators import action
from rest_framework.response import Response
from rating import serializers
from rating.models import Like


# /reviews/<id>?add_to_liked/
@action(['POST'], detail=True)
def add_to_liked(self, request, pk):
    movie = self.get_object()
    user = request.user
    if user.liked.filter(movie=movie).exists():
        return Response('This Movie is Already Liked!', status=400)
    Like.objects.create(owner=user, movie=movie)
    return Response('You Liked The Movie', status=201)


# /reviews/<id>?remove_from_liked/
@action(['DELETE'], detail=True)
def remove_from_liked(self, request, pk):
    movie = self.get_object()
    user = request.user
    if not user.liked.filter(movie=movie).exists():
        return Response('You Didn\'t Like This Movie!', status=400)
    user.liked.filter(movie=movie).delete()
    return Response('Your Like is Deleted!', status=204)


@action(['GET'], detail=True)
def get_likes(self, request, pk):
    movie = self.get_object()
    likes = movie.likes.all()
    serializer = serializers.LikeSerializer(likes, many=True)
    return Response(serializer.data)