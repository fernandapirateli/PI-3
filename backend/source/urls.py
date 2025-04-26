from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('students.urls')),
    path('', include('foods.urls')),
]
