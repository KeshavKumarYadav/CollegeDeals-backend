from django.contrib import admin
from core.models import Product, Category, Tag, Wishlist

class TagAdmin(admin.ModelAdmin):
    list_display = ('product', 'tag_arr')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'price')


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Tag, TagAdmin)
# admin.site.register(TaggedItem)
admin.site.register(Wishlist, WishlistAdmin)
