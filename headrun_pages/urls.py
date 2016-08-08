
from django.conf.urls import include, url, handler404, handler500
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'headrun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    #url(r'^index.html$', views.index, name='index'),
    #url(r'^about.html$', views.about, name='about'),
    #url(r'^portfolio3.html$', views.portfolio3, name='portfolio3'),
]

handler404 = 'headrun_pages.views.error404'
