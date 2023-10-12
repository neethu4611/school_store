from .models import Department,Course,Purpose
def menu_links(request):
    links=Department.objects.all()
    return dict(links=links)
def course(request):
    cou=Course.objects.all()
    return dict(cou=cou)
def reg_data(request):
    register = Purpose.objects.all()
    return dict(register=register)
