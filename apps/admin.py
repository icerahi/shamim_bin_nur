from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from apps.models import Category, Stock, Sell_History
admin.site.site_title="team ICecream";
admin.site.site_header="Team IceCream Production";


class Sell(admin.ModelAdmin):
    list_display=['customar_name','item_name','price','quantity']
    search_fields=['customar_name','item_name','price','quantity']
    list_filter=(('data',DateRangeFilter),
    )


class Register(admin.ModelAdmin):
    list_display = ['item','quantity']

admin.site.register(Category)
admin.site.register(Stock,Register)

admin.site.register(Sell_History,Sell)