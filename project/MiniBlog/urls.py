from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='blogs'),
    path('account/', include('django.contrib.auth.urls')),
    path('accont/register', views.Registration.as_view(), name='registration'),
    path('<int:pk>/', views.PostDetail.as_view(), name='blog_detail'),
    path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
]