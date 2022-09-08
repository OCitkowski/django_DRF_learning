from django.contrib import admin
from .models import Test, CommentTest

class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'quality', 'date_update')
    list_display_links = ('id', 'title', 'date_update')
    search_fields = ('title',)
    #
    # prepopulated_fields = {"slug": ("title",)}

class CommentTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'test')
    list_display_links = ('id', 'title', 'test')
    search_fields = ('title',)
    # prepopulated_fields = {"test": ("title",)}
    # list_editable = ('title', 'text')

admin.site.register(Test, TestAdmin)
admin.site.register(CommentTest, CommentTestAdmin)
