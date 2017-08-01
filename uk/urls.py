from django.conf.urls import patterns, url
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = patterns(
    '',
    url(r'^/?$', RedirectView.as_view(url='https://www.personalgenomes.org.uk', permanent=True),
        name='index'),
    url(r'^/about/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/about', permanent=True),
        name='about'),
    url(r'^/people/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/people', permanent=True),
        name='people'),
    url(r'^/sign-up/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/sign-up', permanent=True),
        name='sign-up'),
    url(r'^/data/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/data', permanent=True),
        name='data'),
    url(r'^/news-archive/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/news-archive', permanent=True),
        name='news-archive'),
    url(r'^/news/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/news', permanent=True),
        name='news'),
    url(r'^/global-network/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/global-network', permanent=True),
        name='global-network'),
    url(r'^/contact-us/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/contact-us', permanent=True),
        name='contact-us'),
    url(r'^/email-storm-incident-and-apology-message/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/archive/email-storm-incident-and-apology-message', permanent=True),
        name='email-storm-incident-and-apology-message'),
    url(r'^/email-storm-incident-and-apology/?', RedirectView.as_view(url='https://www.personalgenomes.org.uk/archive/email-storm-incident-and-apology', permanent=True),
        name='email-storm-incident-and-apology'),
    )
