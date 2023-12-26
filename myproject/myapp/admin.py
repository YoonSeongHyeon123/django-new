from django.contrib import admin
from .models import Blog
from .models import notice
from .models import communicate
# Register your models here.
admin.site.register(Blog)
admin.site.register(notice)
admin.site.register(communicate)