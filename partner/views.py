from django.shortcuts import render
from .models import PartnerModel
from .serializers import PartnerSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
import requests
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def partner_list(request):
    url = 'http://127.0.0.1:8000/partner/api/'
    response = requests.get(url)
    partners = response.json()
    context = {
        'partners':partners
    }
    return render(request,'partner/partner.html',context)
@permission_classes([IsAuthenticated])
@api_view(['get','post'])
def list_api(request):
    partners = PartnerModel()
    if request.method == "GET":
        partners = PartnerModel.objects.all()
        serializer = PartnerSerializer(partners,many = True)
        return Response(data=serializer.data)

    if request.method == "POST":
        serializer = PartnerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['get','put','delete'])
def partner_detail(request,id):
    try:
        model = PartnerModel.objects.get(id=id)
    except PartnerModel.DoesNotExist:
        return Response(data = {'errors':'invalid'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = PartnerSerializer(model)
        return Response(data=serializer.data)
    if request.method == "PUT":
        serializer = PartnerSerializer(model,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if requests.method == "delete":
        model.delete()
        return Response()
        