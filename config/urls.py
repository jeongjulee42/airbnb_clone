
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("users/", include("users.urls", namespace="users")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("reservations/", include("reservations.urls", namespace="reservations")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("lists/", include("lists.urls", namespace="lists")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
