"""likelion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog import views
# import
from django.conf import settings
# import
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('<int:item_id>/', views.list, name="list"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    # category_id 도 같이 보내줌
    path('post_like_toggle/<int:item_id>/<int:category_id>',views.post_like_toggle,name="post_like_toggle"),
    path('search/',views.search, name="search"),
    path('summernote/',include('django_summernote.urls')),
    path('write/',views.write,name="write"),
    path('detail/<int:post_id>',views.detail,name="detail"),
    path('detail/<int:post_id>/comment',views.comment_write,name="comment"),
    path('detail/<int:post_id>/delete_comment/<int:item_id>',views.comment_delete,name="delete"),
    path('detail/<int:post_id>/update_comment/<int:item_id>',views.comment_update,name="update"),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)