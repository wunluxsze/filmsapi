from django.contrib import admin
from .models import Afisha, Films, Genre, Director
# Register your models here.
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Afisha)
admin.site.register(Films)
