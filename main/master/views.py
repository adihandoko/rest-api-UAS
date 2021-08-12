from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Pasien
from .serializers import PasienSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class PasienView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        p=Pasien.objects.all()
        serializer = PasienSerializer(p, many=True)
        return Response(serializer.data)

    def post(self, request):
        p=Pasien.objects.create(nama=request.POST['nama'],umur=request.POST['umur'],)
        p.save
        content = {'message': 'saved!'}
        return Response(content)