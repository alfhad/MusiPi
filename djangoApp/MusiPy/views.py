from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.


class AddAFile(APIView):

    def post(self, request):

        filetype = request.data['fileType']
        metadata = request.data['metaData']

        if filetype.lower() == 'song':
            serializer = SongSerializer(data=metadata)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif filetype.lower() == 'podcast':
            serializer = PodcastSerializer(data=metadata)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif filetype.lower() == 'audiobook':
            serializer = AudioBookSerializer(data=metadata)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


class SongApiView(APIView):

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetails(APIView):

    def get_object(self, id):
        try:
            return Song.objects.get(id=id)
        except Song.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def put(self, request, id):
        song = self.get_object(id)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = self.get_object(id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PodcastApiView(APIView):

    def get(self, request):
        podcast = Podcast.objects.all()
        serializer = PodcastSerializer(podcast, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PodcastSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PodcastDetails(APIView):

    def get_object(self, id):
        try:
            return Podcast.objects.filter(id=id)[0]
        except Podcast.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        podcast = self.get_object(id)
        serializer = PodcastSerializer(podcast)
        return Response(serializer.data)

    def put(self, request, id):
        podcast = self.get_object(id)
        serializer = PodcastSerializer(podcast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        podcast = self.get_object(id)
        podcast.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AudioBookApiView(APIView):

    def get(self, request):
        adb = AudioBook.objects.all()
        serializer = AudioBookSerializer(adb, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AudioBookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AudioBookDetails(APIView):

    def get_object(self, id):
        try:
            return AudioBook.objects.get(id=id)
        except AudioBook.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        adb = self.get_object(id)
        serializer = AudioBookSerializer(adb)
        return Response(serializer.data)

    def put(self, request, id):
        adb = self.get_object(id)
        serializer = AudioBookSerializer(adb, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        adb = self.get_object(id)
        adb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
