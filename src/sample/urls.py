"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import home_page,login_page,register_page,details_page,no_details,no_schemes,apply,success_page,scheme_page
from user.views import details_view,scheme_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^login/$',login_page),
	url(r'^register/$',register_page),
	url(r'^$',home_page),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$',auth_views.logout,{'template_name':'home.html'}),
    url(r'^add-details/$',details_page),
    url(r'^view_page/$',details_view),
    url(r'^view_schemes/$',scheme_view),
    url(r'^no-details/$',no_details),
    url(r'^no-schemes/$',no_schemes),
    url(r'^apply/$',apply),
    url(r'^success/$',success_page),
    url(r'^add-schemes/$',scheme_page)

]
