from django.contrib import admin

# Register your models here.

from .models import Organization, Item, Pricing

"""Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""

admin.site.register(Organization)
admin.site.register(Item)
admin.site.register(Pricing)


# class ItemsInline(admin.TabularInline):
#     """Defines format of inline book insertion (used in AuthorAdmin)"""
#     model = Item


# @admin.register(Organization)
# class OrganizationAdmin(admin.ModelAdmin):
#     """Administration object for Author models.
#     Defines:
#      - fields to be displayed in list view (list_display)
#      - orders fields in detail view (fields),
#        grouping the date fields horizontally
#      - adds inline addition of books in author view (inlines)
#     """
#     list_display = ('id', 'name')
#     fields = ['id', 'name']
#     inlines = [ItemsInline]


# class ItemsInstanceInline(admin.TabularInline):
#     """Defines format of inline book instance insertion (used in BookAdmin)"""
#     model = ItemInstanceInline


# class ItemAdmin(admin.ModelAdmin):
#     """Administration object for Book models.
#     Defines:
#      - fields to be displayed in list view (list_display)
#      - adds inline addition of book instances in book view (inlines)
#     """
#     list_display = ('id', 'type', 'description')
#     inlines = [ItemInstanceInline]


# admin.site.register(Item, ItemAdmin)


# @admin.register(ItemInstance)
# class ItemInstanceAdmin(admin.ModelAdmin):
#     """Administration object for BookInstance models.
#     Defines:
#      - fields to be displayed in list view (list_display)
#      - filters that will be displayed in sidebar (list_filter)
#      - grouping of fields into sections (fieldsets)
#     """
#     list_display = ('id', 'type', 'description')
#     list_filter = ('id', 'type')

#     fieldsets = (
#         (None, {
#             'fields': ('id', 'type', 'description')
#         }),
#         ('Availability', {
#             'fields': ('id', 'type', 'description')
#         }),
#     )
