from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('djangotutorial.polls.urls')),  # 👈 this makes homepage open polls
    path('admin/', admin.site.urls),
    path('polls/', include('djangotutorial.polls.urls')),
]
