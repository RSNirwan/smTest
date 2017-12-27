"""mirror URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from django.conf import settings
from django.conf.urls.static import static

from displayWidgets.views import home, get_user_config

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^user/(?P<name>[a-zA-Z0-9]+)/$', home, name='users_config'),
    url(r'^post_config/$', get_user_config, name='post_config'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)