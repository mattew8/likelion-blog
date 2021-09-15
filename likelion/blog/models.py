from django.db import models
from django.db.models.deletion import CASCADE


class Post(models.Model):
    title = models.CharField(max_length=20)  # 글자 수 제한 O
    content = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        "Category", on_delete=CASCADE, related_name="post")

    def __str__(self):
        return self.title


class Category(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject  # admin에서 카테고리의 subject를 보여줄꺼야

# 댓글 -> 하나의 글은 ; 여러개의 댓글 O
# 하나의 카테고리 : 여러개의 Post O

# 1. 데이터 구조변화 기록 -> makemigrations
# 2. 해당 기록들을 실재로 DB에 적용한다 -> migrate

# Create your models here.
