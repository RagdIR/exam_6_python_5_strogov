from django.contrib import admin
from .models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Guestbook, GuestbookAdmin)
