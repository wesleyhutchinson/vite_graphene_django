from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from .api.views import index_view


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("", index_view, name="index")
]

if settings.DEBUG:
    urlpatterns += (path("api/", GraphQLView.as_view(graphiql=True)),)
else:
    urlpatterns += (path("api/", GraphQLView.as_view()),)
