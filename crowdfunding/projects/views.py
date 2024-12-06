from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Band, Tour, Pledge, Genre
from .serializers import BandSerializer, TourSerializer, PledgeSerializer, GenreSerializer, TourDetailSerializer, BandDetailSerializer, GenreDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class TourList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

# TODO limit to usertype bandmember only    
    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TourDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            title = Tour.objects.get(pk=pk)
            self.check_object_permissions(self.request, title)
            return title
        except Tour.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        title = self.get_object(pk)
        serializer = TourDetailSerializer(title)
        return Response(serializer.data)

    def put(self, request, pk):
        title = self.get_object(pk)
        serializer = TourDetailSerializer(
            instance=title,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        band = self.get_object(pk)
        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BandList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        band = Band.objects.all()
        serializer = BandSerializer(band, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = BandSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class BandDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            band = Band.objects.get(pk=pk)
            self.check_object_permissions(self.request, band)
            return band
        except Band.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        band = self.get_object(pk)
        serializer = BandDetailSerializer(band)
        return Response(serializer.data)

# TODO limit to usertype bandmember only
    def put(self, request, pk):
        
        band = self.get_object(pk)
        serializer = BandDetailSerializer(
            instance=band,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        band = self.get_object(pk)
        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreList(APIView):
# TODO limit to superuser / admin only
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class  GenreDetail(APIView): 
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            genre = Genre.objects.get(pk=pk)
            self.check_object_permissions(self.request, genre)
            return genre
        except Band.DoesNotExist:
            raise Http404
  
    def get(self, request, pk):
        genre = self.get_object(pk)
        serializer = GenreDetailSerializer(genre)
        return Response(serializer.data)
    
    def put(self, request, pk):
        name = self.get_object(pk)
        serializer = GenreDetailSerializer(
            instance=name,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
