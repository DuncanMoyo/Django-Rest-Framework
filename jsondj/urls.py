from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import blog_list, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_list),
    url(r'^home', home),
    url(r'api/', include('blog.api.urls', namespace='api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
