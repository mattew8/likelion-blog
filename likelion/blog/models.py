from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import related

class Profile(models.Model):
    # user one to one 
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # 내가 좋아요한 포스트 >> 해당 프로필 유저가 좋아요한 포스트들을 접근할 수 있는 필드
    like_post = models.ManyToManyField('Post',blank=True,related_name="like_users")
    def __str__(self):
        return str(self.user)

class Post(models.Model):
    # profile F.K
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="profile_user")
    title = models.CharField(max_length=20)  # 글자 수 제한 2O
    content = models.TextField()
    # image add
    image = models.ImageField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "Category", on_delete=CASCADE, related_name="post")
    # 양수만 반환하는 좋아요 수 카운트 필드
    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title


class Category(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject  # admin에서 카테고리의 subject를 보여줄꺼야

# 댓글 -> 하나의 글은 ; 여러개의 댓글 O
# 하나의 카테고리 : 여러개의 Post O
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=CASCADE,related_name='post_comment')
    author = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    content = models.TextField(max_length=300)

    def __str__(self):
        return str(self.post)








# 1. 데이터 구조변화 기록 -> makemigrations
# 2. 해당 기록들을 실재로 DB에 적용한다 -> migrate

# Create your models here.
