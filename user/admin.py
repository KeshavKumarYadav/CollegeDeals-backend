from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ua
from user.models import User, Block, District, State, Address, Institute

class UserAdmin(ua):
    list_display = ('email', 'last_login', 'is_admin', 'is_staff', 'is_superuser', 'institute', 'hide_email')
    search_fields = ('email',)
    readonly_fields = ('id','last_login', 'joined')
    ordering = ('email',)

    # fieldsets = ua.fieldsets + (
    #     (None, {'fields': ('email',)}),
    # )
    add_fieldsets = (
            (None, {'fields': ('email', 'password1', 'password2',
                               'is_active', 'is_staff', 'is_superuser', 'institute', 'hide_email')}),
        )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)
admin.site.register(Block)
admin.site.register(District)
admin.site.register(State)
admin.site.register(Address)
admin.site.register(Institute)
