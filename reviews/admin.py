from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'job_status','review_date', 'reply', 'replies_from_employer', 'test_tasks', 'offers')
    search_fields = ('text',)
    list_filter = ('review_date',)
    empty_value_display = '-пусто-'
    ordering = ('-review_date',)

admin.site.register(Review, ReviewAdmin)
