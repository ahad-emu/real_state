from django.shortcuts import render
from listings.models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import bedroom_choices, state_choices, price_choices

# Create your views here.
def index(request):
    items = Listing.objects.order_by('-list_date').filter(is_published=True)
    #paginator
    paginator = Paginator(items, 6)
    page = request.GET.get('page')
    paged_item = paginator.get_page(page)

    context = {
        'listings': paged_item ,
    }

    return render(request, "listings/listings.html", context)

def listing(request, Listing_id):
    item = Listing.objects.get(pk = Listing_id)

    context = {
        'item': item ,
    }

    return render(request, "listings/listing.html" , context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)


    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    context = {
        'bedroom_choices' : bedroom_choices ,
        'state_choices' : state_choices ,
        'price_choices' : price_choices ,
        'listings' : queryset_list,
    }
    return render(request, "listings/search.html", context)
