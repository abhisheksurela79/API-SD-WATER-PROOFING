from django.contrib import admin
from .models import Images, Videos, PDF


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'image', 'uploaded_at')
    list_display_links = ('heading', 'image')


class VideosAdmin(admin.ModelAdmin):
    list_display = ('heading', 'video', 'uploaded_at')
    list_display_links = ('heading', 'video')


class PDFAdmin(admin.ModelAdmin):
    list_display = ('heading', 'pdf', 'uploaded_at')
    list_display_links = ('heading', 'pdf')


# Register the custom admin class for Images model
admin.site.register(Images, ImagesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(PDF, PDFAdmin)
