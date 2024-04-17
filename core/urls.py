from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import blog_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_home, name='home'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('comments/', include('comments.urls', namespace='comments')),
    path("__reload__/", include("django_browser_reload.urls"))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)