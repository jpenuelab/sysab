from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import TbEps
from .serializers import TbEpsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.


# class EpsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, 
#                 mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     serializer_class = TbEpsSerializer
#     queryset = TbEps.objects.all()

class EpsViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    serializer_class = TbEpsSerializer
    queryset = TbEps.objects.all()

    
    



class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, 
                    mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = TbEpsSerializer
    queryset = TbEps.objects.all()

    lookup_field = 'id_eps'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_eps=None):

        if id_eps:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id_eps=None):
        return self.update(request, id_eps)

    def delete(self, request, id_eps):
        return self.destroy(request, id_eps)


class EpsAPIView(APIView):

    def get(self, request):
        eps = TbEps.objects.all()
        serializer = TbEpsSerializer(eps, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TbEpsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class EpsDetails(APIView):

    def get_obeject(self, id_eps):
        try:
           return TbEps.objects.get(id_eps=id_eps)

        except TbEps.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id_eps):
        eps = self.get_obeject(id_eps)
        serializer = TbEpsSerializer(eps)
        return Response(serializer.data)

    def put(self, request, id_eps):
        eps = self.get_obeject(id_eps)
        serializer = TbEpsSerializer(eps, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status_400_BAD_REQUEST)

    def delete(self, request, id_eps):
        eps = self.get_obeject(id_eps)
        eps.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





"""


@api_view(['GET','POST'])
def eps_list(request):
    if request.method == 'GET':
        eps = TbEps.objects.all()
        serializer = TbEpsSerializer(eps, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TbEpsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def eps_detail(request, pk):
    try:
        eps = TbEps.objects.get(pk=pk)

    except TbEps.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TbEpsSerializer(eps)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TbEpsSerializer(eps, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        eps.delete()
        return HttpResponse(status=204)
"""






