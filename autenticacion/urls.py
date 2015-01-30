from django.conf.urls import patterns, url
from .views import RootView, LoginView, LogoutView, DelTokenView, GetTokenView


routerToken = patterns(
    '',
    url(r'^$', RootView.as_view(), name='root'),
    url(r'^token/login$', GetTokenView.as_view(), name='getToken'),
    url(r'^token/logout$', DelTokenView.as_view(), name='delToken'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
)
