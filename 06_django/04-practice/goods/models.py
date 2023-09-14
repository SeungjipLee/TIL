from django.db import models

# Create your models here.
# class명 convention
# 모델 정의 -> 아이디어 스케치
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField()
    # 생성일자 = DateField | YYYY-MM-DD | '2023-11-11'
    # auto_now_add => 데이터 생성 시점의 날짜를 자동으로 입력
    # makemigrations를 통해 추가된 column을 기존 table에 적용시키려고 하니까
    # 이전에 만들어진 데이터들은 생성된 시점을 알 수가 없다.
        # default값을 설정할수는 없되
        # 기존 데이터들에게 넣어줄 값들은 설정해 줘야 한다.
    created_at = models.DateField(auto_now_add=True)
    # 수정일자
    updated_at = models.DateTimeField(auto_now=True)
    
    # 사람이 보기 좋게 출력 결과를 판단하는 메서드
    def __str__(self):
        return self.name

# 설계도 만들기 -> makemigrations
# 설계도를 기반으로 실제 db(각 테이블) 생성하기 -> migrate

'''
# product1 = Product(
                name='피카츄',
                description='귀엽다',
                price=12200,
                is_published=False
            )
'''

