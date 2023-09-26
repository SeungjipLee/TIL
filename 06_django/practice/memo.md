1. gitignore 만들기(gitignore.io)
2. 가상환경 만들기(python -m venv venv)
3. 가상환경 켜기(source ~~)
4. pip install(django)
5. pip freeze > requirements.txt(구성 환경 기록하기)
6. django-admin startproject menu_management .(프로젝트 생성)
7. python manage.py startapp menus(앱 생성)
8. application 등록(project - setting 에서 쉼표까지 제대로 달아서 추가)
9. Menu model을 정의한다.(모든 시작은 모델 만들기 - 앱 안의 models.py에서)
  ```python
  class Menu(models.Model):
      name = models.CharField(max_length=100)
      price = models.IntergerField()
      description = models.TextField()
      is_vegan = models.BooleanField()
  ```
10. 1 - 설계도 작성 => 2 - 테이블 작성
  1. python manage.py makemigrations
  2. python manage.py migrate

11. 프로젝트안의 urls.py에서 원래 작업하였으나, 앱 안에서 각자 처리할 수 있도록
  1. path('menus/', include('menus.urls'))를 프로젝트 urls에 추가(import도 당연히)
  2. 앱 안에서 따로 처리할 것이므로 앱 안의 urls.py를 생성한다.
    ```python
    from django.urls import path
    from . import views

    app_name = 'menus'
    urlpatterns = [
        path('', view.index, name = 'index')
    ]
    ```
12. views.py 에서 index함수 정의
13. 앱(메뉴스) 안에 템플릿에 메뉴스에 인덱스 HTML만들기
14. 베이스 템플릿 만들기(최상위 폴더에 템플릿 - base.html) 블록 자리 두기
15. 다시 앱 안의 index.html에서 extends하고 block자리에 내용 넣기
16. CREATE 만들기(new기능)
17. new (url -> view -> html 순서로 만들기)
  -> html에 일일히 적다보니 너무 귀찮고 많음
  -> modelform으로 받기 위해 forms.py를 만든다.
18. new.html에 view에서 만든 변수들 사용