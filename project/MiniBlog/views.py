from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Likes
from .forms import CommentsForm, RegistrationUserForm


# Create your views here.
class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'MiniBlog/blog.html', context)


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = CommentsForm()
        return render(request, 'MiniBlog/blog_detail.html', {'post': post, 'form': form})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')


class Registration(View):
    def get(self, request):
        form = RegistrationUserForm()
        context = {
            'form': form,
        }
        return render(request, 'registration/register.html', context)