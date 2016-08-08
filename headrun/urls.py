from django.conf.urls import include, url
from django.conf.urls import handler404
from django.contrib import admin
import headrun_pages


urlpatterns = [
    # Examples:
    # url(r'^$', 'headrun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('headrun_pages.urls')),
    url(r'^index.html$', headrun_pages.views.index, name='index'),
    url(r'^contact.html$', headrun_pages.views.contact, name='contact'),

    url(r'^contact.php.*', headrun_pages.views.contact_, name='contact_'),
    url(r'^portfolio_services.html$', headrun_pages.views.portfolio3, name='portfolio3'),
    url(r'^about.html$', headrun_pages.views.about, name='about'),
    url(r'^testimonials.html$', headrun_pages.views.testimonials, name='testimonials'),
    url(r'^services.html$', headrun_pages.views.services, name='services'),
    url(r'^timeline.html$', headrun_pages.views.timeline, name='timeline'),
    url(r'^buzzinga.html$', headrun_pages.views.buzzinga, name='buzzinga'),
    url(r'^blackbuck.html$', headrun_pages.views.blackbuck, name='blackbuck'),
    url(r'^miebach.html$', headrun_pages.views.miebach, name='miebach'),
    url(r'^floretz.html$', headrun_pages.views.floretz, name='floretz'),
    url(r'^tlg.html$', headrun_pages.views.tlg, name='tlg'),
    url(r'^notemonk.html$', headrun_pages.views.notemonk, name='notemonk'),
    url(r'^crawl$', headrun_pages.views.profile, name='profile'),
    url(r'^incog.html$', headrun_pages.views.incog, name='incog'),
    url(r'^cloudlibs.html$', headrun_pages.views.cloudlibs, name='cloudlibs'),
    url(r'^juicer.html$', headrun_pages.views.juicer, name='juicer'),
    url(r'^paymentgateway.html$', headrun_pages.views.paymentgateway, name='paymentgateway'),
    #url(r'^admin/', include(admin.site.urls)),

]

handler404 = 'headrun_pages.views.error404'
