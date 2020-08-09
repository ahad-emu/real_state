from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def home(request):
    items = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    return render(request, "pages/home.html", {'items': items})


def about(request):
    realtors = Realtor.objects.order_by('-hired_date')

    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    return render(request, "pages/about.html", {'realtors': realtors, 'mvp_realtors': mvp_realtors})
