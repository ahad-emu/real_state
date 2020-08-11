from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, state_choices, price_choices

# Create your views here.
def home(request):
    items = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'items' : items ,
        'bedroom_choices' : bedroom_choices ,
        'price_choices' : price_choices ,
        'state_choices' : state_choices ,
    }

    return render(request, "pages/home.html", context)


def about(request):
    realtors = Realtor.objects.order_by('-hired_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors' : realtors ,
        'mvp_realtors' : mvp_realtors ,
    }

    return render(request, "pages/about.html", context)
