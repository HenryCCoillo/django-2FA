
from django.contrib import admin
from django.urls import path,include
from twofa.views import Home, Dashboard,RegisterView,SignOff
from two_factor.urls import urlpatterns as tf_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(), name='home'),
    path('', include(tf_urls)),
    path('dashboard/',Dashboard.as_view(), name='dashboard'),
    path('dashboard/',Dashboard.as_view(), name='dashboard'),

    path('signup/',RegisterView.as_view(),name="signup"),
    path('signoff/',SignOff,name='signoff'),

]
