from django.contrib import admin
from .models import App
from .models import User
from .models import Review,blockwords

# Register your models here.
admin.site.register(App)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(blockwords)