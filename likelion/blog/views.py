from django.shortcuts import render
from .models import Post, Category


def index(request):
    # 모든 카테고리를 인덱스 페이지에 뿌려준다
    categories = Category.objects.all()

    context = {"categories": categories}

    return render(request, "index.html", context)


def list(request, item_id):
    selected_category = Category.objects.get(pk=item_id)
    # 카테고리 데이터에서 pk가 item_id인 카테고리 하나만 가져왔다
    posts = selected_category.post.all()
    # 선택된 카테고리에 해당하는 posts들을 전부다 가져왔다

    context = {"selected_category": selected_category, "posts": posts}

    return render(request, "list.html", context)


# Create your views here.
