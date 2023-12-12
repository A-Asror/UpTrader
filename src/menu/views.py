from django.shortcuts import render


def menu_view(request, menu_name=None):
    return render(request, 'main_page.html', {'menu_name': menu_name})
