from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Correct path to polls app
    path("polls/", include("djangotutorial.polls.urls")),
]
