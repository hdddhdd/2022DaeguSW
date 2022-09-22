from django.shortcuts import render

def index(request):
	return render(request, 'core/index.html')


def login(request):
	return render(request, 'core/login.html')

#예제 코드
def example(request):
	return render(request, 'core/example.html')