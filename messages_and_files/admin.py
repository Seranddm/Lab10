from django.contrib import admin

from messages_and_files.models import Message

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('text_of_question', 'author', 'is_published')
#     list_display_links = ('text_of_question', )
#     search_fields = ('text_of_question', )


admin.site.register(Message)