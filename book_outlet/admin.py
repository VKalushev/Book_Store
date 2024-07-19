from django.contrib import admin

from .models import Book,Author,Address,Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {'slug': ("title",)}
    list_filter = ("author","rating")
    list_display = ("title", "author")

class AuthorAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    list_filter = ("first_name","last_name")
    list_display = ("first_name","last_name", "address")

class AddressAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    list_filter = ("city","postal_code")
    list_display = ("city","postal_code")

class CountryAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    list_filter = ("name",)
    list_display = ("name","code")


admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Country,CountryAdmin)