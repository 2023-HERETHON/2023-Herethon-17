from django.shortcuts import render

def home(request):
    return render(request, 'mainPage.html')

# Post페이지로 넘어올 땐 게시글 번호 필요함
def post(request): 
    return render(request, 'post.html')

def detail(request):
    return render(request, 'postDetail.html')


