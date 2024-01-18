from .models import *

def menu_links(request):
    links = Product.objects.all()
    return dict(links=links)