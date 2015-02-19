from django.conf.urls import patterns, url
from .views import RootView, LoginView, LogoutView

routerToken = patterns(
    '',
    url(r'^$', RootView.as_view(), name='root'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
)
