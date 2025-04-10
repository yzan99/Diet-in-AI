
from django.contrib import admin
from django.urls import path, include
from diet import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path("",views.index,name="index" ),
    # path("home/",views.HOME,name="home" ),
    # path('about/',v.ABOUTUS, name="ABOUTUS"),
    # path('contact/',v.CONTACTUS, name="CONTACTUS"),
    # path("home/", include("translationSite.urls",namespace='translation')),
    path ("form/",views.form,name="form"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    