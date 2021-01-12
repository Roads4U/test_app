from django.conf.urls import url, include
# from two_factor.urls import urlpatterns as tf_urls
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView,PasswordResetView,PasswordResetConfirmView,PasswordResetCompleteView
from dshbrd import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    url(r'home$', views.data_population_p, name="home"),
    url(r'call', views.data_population_aj, name="call"),
    url(r'^admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'))

    ]


