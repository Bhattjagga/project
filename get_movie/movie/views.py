import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from movie.models import MoviesDetails
from datetime import datetime
from .serializer import MovieDetailSerialize

# Create your views here.
@api_view(['GET'])
def getMovieDetails(request):
    if request.method=='GET':
        id=request.GET.get('id')
        year=request.GET.get('year')
        genre=request.GET.get('genre')
        user_rating=request.GET.get('rating')
        title=request.GET.get('title')
        key=request.GET.get('key')
        print(key,title,'&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        if id:
            try:
                obj=MoviesDetails.objects.get(id=id)
                sez=MovieDetailSerialize(obj)
            except:
                obj=None
        elif title:
           
            obj=MoviesDetails.objects.filter(title=title)
            sez=MovieDetailSerialize(obj,many=True)
        elif genre:
            obj=MoviesDetails.objects.filter(genre__icontain=genre)
            sez=MovieDetailSerialize(obj,many=True)
        elif year:
            obj=MoviesDetails.objects.filter(release_year__year__gte=year)
            sez=MovieDetailSerialize(obj,many=True)
        elif user_rating:
            obj=MoviesDetails.objects.filter(rating__gte=user_rating)
            sez=MovieDetailSerialize(obj,many=True)
        else:
            pass
        
        if obj:
            return Response({
                                'status':1,
                                'message':'Successfully ! fatch data! ',
                                'data':sez.data
                                                
                                })
        else:
            r =requests.get(f'http://www.omdbapi.com/?apikey={key}&t={title}', params=request.GET)
            data = r.json()
            title=data['Title']
            relase=data['Released']
            genres=data['Genre']
            actor=data['Actors']
            director=data['Director']
            rating=data['Ratings'][0]['Value']
            language=data['Language']
            d=datetime.strptime(relase, '%d %B %Y')
            rate=rating.split('/')[0]
            obj=MoviesDetails.objects.create(title=title,release_year=d,genres=genres, director=director,
            actor=actor,language=language,rating=rate)

            return Response({
                                'status':1,
                                'message':'Successfully ! fatch data ',
                                'data':{'Title':title,'Released':relase,'Genre':genre,'Rating':rate}
                                                
                                })

        

        