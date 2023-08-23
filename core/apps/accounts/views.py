from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.apps.accounts.forms import UserRegisterForm
from .serializers import UserSerializer


@api_view(['GET'])
def users(request):
    queryset = User.objects.all()
    serializer_for_queryset = UserSerializer(
        instance=queryset,
        many=True
    )
    return Response(serializer_for_queryset.data)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.data)
        if form.is_valid():
            form.save()
            return Response('OK')
        return Response('NO OK')


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        user = authenticate(request.data, username=request.data['username'], password=request.data['password'])
        if user is not None:
            auth_login(request, user)
            return Response('OK')
        return Response('NO OK')


@login_required
@api_view(['GET'])
def profile(request):
    queryset = User.objects.get(id=request.user.id)
    serializer_for_queryset = UserSerializer(
        instance=queryset
    )
    return Response(serializer_for_queryset.data)

