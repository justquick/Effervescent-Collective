from django.contrib import admin
from models import Term

class TermAdmin(admin.ModelAdmin):
    change_list_template = 'terminal/change_list.html'

admin.site.register(Term, TermAdmin)