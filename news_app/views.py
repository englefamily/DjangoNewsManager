from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponsePermanentRedirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import PostForm, CreateUser
from .models import NewsPost
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required, login_required
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from .serializers import post_serializer


# Create your views here.

class Create_post(CreateView):
    model = NewsPost
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = '/posts_list'


@permission_required('news_app.view_newspost', login_url='/access_denied/view')
def List_post(req):
    list_post = NewsPost.objects.all()
    return render(request=req, template_name='posts_list.html', context={'posts': list_post})


@permission_required('auth.add_user', login_url='/access_denied/view')
def create_user(req):

    if req.method == 'GET':
        return render(request=req, template_name='registration/signup.html', context={'form': CreateUser()})

    if req.method == 'POST':
        user_form = CreateUser(data=req.POST)

        if user_form.is_valid():
            new_user = user_form.save()
            new_user_token = Token(user=new_user)
            new_user_token.save()

            login(request=req, user=new_user)
            return redirect('/create_post/')
        else:
            return render(request=req, template_name='registration/signup.html'
                                                     'signup.html', context={'form': user_form})


@require_http_methods('GET')
def base(req):
    if req.user.is_authenticated:
        return redirect('/create_post')
    return render(request=req, template_name='base.html')


@api_view(['GET', 'POST'])
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def auth_test(request):
    # return render(request=request, template_name='test_auth.html')
    return Response(status=status.HTTP_200_OK, data={'success': True})


def no_perms(req, perm_name):
    return HttpResponse(f'<h1>You do not have permission to {perm_name} this page.</h1>')

def edit_post(req, id_):
    if req.method == 'GET':
        # a = id_
        post_ = NewsPost.objects.filter(pk=id_)
        if post_:
            post_form = PostForm(instance=post_[0])
            return render(request=req, template_name='edit_post.html', context={'post_form': post_form, 'id': id_})
        return HttpResponse('The article does not exist.')

    if req.method == 'POST':
        pass

def serve_ynet(request):
    posts = NewsPost.objects.all()
    post_sr = [post_serializer(post) for post in posts]
    return JsonResponse({"posts": str(post_sr)})

