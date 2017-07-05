from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import settings
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^product/$', views.ProductView.as_view(), name='about'),
    url(r'^blogdetail/$', views.BlogDetailView.as_view(), name='blogdetail'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
