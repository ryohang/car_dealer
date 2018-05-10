from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CarList

urlpatterns = [
    url(r'^cars$', CarList.as_view()),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
