from django.contrib import admin
from django.urls import path,include
import school_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('school_app.urls'))
]
