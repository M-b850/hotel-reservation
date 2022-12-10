from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from hotels.views import Index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Index.as_view()),
    path("hotels/", include("hotels.urls")),
    path("accounts/", include("accounts.urls")),
    path("reservation/", include("reservation.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
