from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate,logout
#from .forms import RegistrationForm, LoginForm
#from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from elearning_app.serializers import LoginSerializer
from elearning_app.models import Login, UserTypes


@api_view(['POST'])
def signup(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        role = request.data.get('role', UserTypes.STUDENT)
        user = User.objects.create_user(
            username=request.data['username'],
            password=request.data['password'],
            email=request.data.get('email', ''),
            role=role,
        )

        # Automatically create a Login entry
        login = Login(email=user.email, role=role, password=user.password)
        login.save()

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': serializer.data, 'role': role}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # Check if the input is an email
    if '@' in email:
        user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)
        serializer = LoginSerializer(user)
        return Response({'token': token.key, 'user': serializer.data, 'role': user.role}, status=status.HTTP_200_OK)

    return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Token is valid. You are authenticated!", status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    # Perform any additional actions you need before logging out (optional)
    # ...

    # Log the user out
    logout(request)

    return Response("Successfully logged out.", status=status.HTTP_200_OK)





"""""
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log in the user after registration
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('test_token')  # Redirect to a page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('test_token')  # Redirect to a page after successful login
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

"""