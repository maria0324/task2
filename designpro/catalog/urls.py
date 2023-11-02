
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
                  path('', ViewRequests.as_view(), name='index'),
                  path('register/', RegistrateUser.as_view(), name='registration'),
                  path('login/', BBLoginView.as_view(), name='login'),
                  path('logout/', BBLogoutView.as_view(), name='logout'),
                  path('request/create', CreateRequest.as_view(), name='request_create'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



