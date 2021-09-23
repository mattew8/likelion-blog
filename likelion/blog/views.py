from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required

def index(request):
    # 모든 카테고리를 인덱스 페이지에 뿌려준다
    categories = Category.objects.all()

    context = {"categories": categories}

    return render(request, "index.html", context)


def list(request, item_id):
    # 카테고리 데이터에서 pk가 item_id인 카테고리 하나만 가져왔다
    selected_category = Category.objects.get(pk=item_id)
   
    # 선택된 카테고리에 해당하는 posts들을 전부다 가져왔다
    posts = selected_category.post.all()
    # 요청된 유저 
    user = request.user
    # 요청된 유저의 profile
    profile = Profile.objects.get(user=user)
    
    context = {"selected_category": selected_category, "posts": posts,'profile':profile}

    return render(request, "list.html", context)





@login_required(login_url='/login')
def post_like_toggle(request,item_id,category_id):
    #해당 id 값을 가진 post 를 들고오기
    post = Post.objects.get(id=item_id)
    # 현재 요청된 유저 (로그인된 유저) 들고오기
    user =request.user
    profile = Profile.objects.get(user=user)
    
    # 해당 유저가 post 를 좋아요했는지 안했는지 check
    check_like_post = profile.like_post.filter(id=item_id)
    # 존재하면 >> 이미 좋아요를 눌렀기 때문에 post 좋아요 취소 하고, 좋아요 수 -1
    if check_like_post.exists():
        profile.like_post.remove(post)
        post.like_count -=1
        post.save()
    # 존재하지 않으면 >> 좋아요를 누를거기 때문에, 좋아요 해주고, 좋아요 수 +1
    else:
        profile.like_post.add(post)
        post.like_count +=1
        post.save()
    # post id 로 가는게 아니라 해당 카테고리로 가야함.
    return redirect('list',category_id)


# def search(request):
#     # id값으로 내림차순
#     post_list = Post.objects.order_by('-id')
#     # q 값이 없으면 빈문자열 리턴
#     # ?=q get 방식
#     search_keyowrd = request.GET.get('q','')
 
#     if search_keyowrd:
#         # icontaines 는 대소문자 구분없이
#         post_list = post_list.filter(title__icontains = search_keyowrd)| post_list.filter(content__icontains = search_keyowrd)
#         return render(request,'search.html',{'post_list':post_list})
#     else:
#         return render(request,'search.html')
   

def search(request):
    post_list = Post.objects.order_by('-id')
    search_keyword = request.GET.get('q','')
    # 해당 인풋에 적은 검색 키워드가 있으면
    if search_keyword:
        # title,content 에 search keyword 가 있는 post 오브젝트들만 가지고 와주세여
        post_list = post_list.filter(title__icontains = search_keyword)| post_list.filter(content__icontains = search_keyword)
        return render(request,'search.html',{'post_list':post_list})
    # 없으면 그냥 search.html render
    else:
        return render(request,'search.html')

   
