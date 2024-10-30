from django.contrib import admin
from giftshopapp.models import user,product,wishlist,cart


# Register your models here.
admin.site.register(user)
admin.site.register(product)
admin.site.register(wishlist)
admin.site.register(cart)

# @admin.register(login)
# class loginAdmin(admin.ModelAdmin):
    # list_display=['name','email','password']

fields = ( 'image_tag', )
readonly_fields = ('image_tag',)
