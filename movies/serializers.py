from rest_framework import serializers
from .models import Movie, Actor, Review
from rest_framework.validators import UniqueValidator




class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[UniqueValidator(
            queryset=Movie.objects.all(),
            message='이미 존재하는 영화 이름입니다.',
        )])
    # movie_reviews = serializers.PrimaryKeyRelatedField(source='reviews', many=True, read_only=True)
    reviews = serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'name', 'reviews','opening_date', 'running_time', 'overview']



class ReviewSerializer(serializers.ModelSerializer):
    # movie = serializers.StringRelatedField()
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
        extra_kwargs = {
            'movie': {'read_only': True},
        }

class ActorSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date']
