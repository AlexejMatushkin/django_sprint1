from django.shortcuts import render


def about(request):
    """Выводит страницу с информацией о проекте."""
    return render(request, 'pages/about.html')


def rules(request):
    """Выводит страницу с правилами проекта."""
    return render(request, 'pages/rules.html')