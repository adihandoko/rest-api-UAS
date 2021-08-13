from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Pasien
from .serializers import PasienSerializer
from rest_framework.pagination import PageNumberPagination

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50


class PasienView(APIView,):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        p=Pasien.objects.all()
        serializer = PasienSerializer(p, many=True)\

        return Response(serializer.data)

    def post(self, request):
        p=Pasien.objects.create(nama=request.POST['nama'],umur=request.POST['umur'],)
        p.save
        content = {'message': 'saved!'}
        return Response(content)

class PasienPageView(APIView,):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        limit=int(request.GET['limit'])
        offset=int(request.GET['offset'])
        p=Pasien.objects.all()[offset:offset+limit]
        serializer = PasienSerializer(p, many=True)

        return Response(serializer.data)

    def post(self, request):
        p=Pasien.objects.create(nama=request.POST['nama'],umur=request.POST['umur'],)
        p.save
        content = {'message': 'saved!'}
        return Response(content)