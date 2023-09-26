from django.shortcuts import render, redirect
from .models import Menu
from .forms import MenuForm


# Create your views here.
# 전체 메뉴 목록을 확인 할 수 있어야 한다.
# -> Menu 테이블에 들어있는 데이터 모두 가져오기/
def index(request):
    # db로 부터 Menu 테이블에 있는 모든 데이터 '조회'
    # SQL을 대신하는 ORM을 사용해서 가져온다.
    # Menu에 대한 접근은 무엇으로 하느냐?
    # class.manager.query Set API
    # 메뉴, 모든 객체 대상 매니저, 전체 데이터 조회()
    menus = Menu.objects.all()
    # 파이썬에서 정의한 데이터를 html에서 DTL 형태로 쓸 수 있도록
    # render 함수가 html을 잘 랜더링 할 수 있도록
    context = {
        'menus': menus,
    }
    return render(request, 'menus/index.html', context)


def detail(request, pk):
    menu = Menu.objecs.get(pk=pk)
    context = {
        'menu':menu,
    }
    return render(request, 'menus/detail.html', context)

def new(request):
    # POST방식으로 요청이 왔을 때
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            # POST 요청에 대한 처리는 위에서 마쳤음.
            # 서비스직이란... 하나가 오면 2개를 해줘야 한다.
            return redirect('menus:index')
    else:
    # 사용자가 값을 입력할 수 있는 form을 그려줘야 한다.
    # ModelForm을 사용하지 않으면 직접 form태그를 일일히 다 적어줘야 한다.
        form = MenuForm()
        # print(form)
    context = {
        'form': form
    }
    return render(request, 'menus/new.html', context)