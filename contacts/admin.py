from django.contrib import admin
from contacts.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'listing', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')

admin.site.register(Contact, ContactAdmin)
