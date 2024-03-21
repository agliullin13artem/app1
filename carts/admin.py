from django.contrib import admin

from carts.models import Cart


# дополнительная таблица для огтображения в админ понели
class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'create_timestamp'
    search_fields = 'product', 'quantity', 'create_timestamp'
    readonly_fields = ('create_timestamp', )
    extra = 1 



@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity', 'create_timestamp', ]
    list_filter = ['create_timestamp', 'user', 'product__name', ]

#изменяем название в админ понели
    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return 'Анонимный пользователь' 


    # изменениям название в админ понели
    def product_display(self, obj):
        return str(obj.product.name)
