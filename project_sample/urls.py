from django.views.generic import TemplateView
from django.urls import include, re_path

from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="homepage.html"),),
    re_path(r'^schedule/', include('schedule.urls')),
    re_path(r'^fullcalendar/', TemplateView.as_view(template_name="fullcalendar.html"), name='fullcalendar'),
    re_path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
