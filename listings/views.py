from django.shortcuts import render
from listings.models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    items = Listing.objects.all()
    #paginator
    paginator = Paginator(items, 3)
    page = request.GET.get('page')
    paged_item = paginator.get_page(page)

    return render(request, "listings/listings.html", {'listings': paged_item})

def listing(request, Listing_id):
    item = Listing.objects.get(pk = Listing_id)
    return render(request, "listings/listing.html" , {'item' : item })

def search(request):
    return render(request, "listings/search.html")
