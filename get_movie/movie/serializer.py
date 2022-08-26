from rest_framework import serializers
from movie.models import MoviesDetails



class MovieDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model=MoviesDetails
        fields=['id','title','release_year','genres','rating']