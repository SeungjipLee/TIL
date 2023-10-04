from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # pass
    score = models.IntegerField(default=100)

    # models.py에 User class 정의만 하면 되느냐?
    # django는 기본적으로 Auth.User를 user 모델로 보기 때문에
    # 그냥 makemigrations, migrate 하게 되면 빨간색이 뜬다