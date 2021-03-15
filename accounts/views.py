from django.shortcuts import redirect, render


def login(request):
    if request.method == 'POST':
        # Login User
        pass
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def register(request):
    if request.method == 'POST':
        # Register User
        pass
    else:
        return render(request, 'accounts/register.html')


def dash_board(request):
    return render(request, 'accounts/dash_board.html')
