from rest_framework import serializers
from .models import Movie, Actor, Review
from rest_framework.validators import UniqueValidator


class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(
            queryset=Movie.objects.all(),
            message='이미 존재하는 영화 이름입니다.',
        )])
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
        extra_kwargs = {
            'movie': {'read_only': True},
        }