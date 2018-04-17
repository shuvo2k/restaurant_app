
from django.conf.urls import url
from django.contrib import admin
from foodtaskerapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^resturant/sign-in/$', auth_views.login,
    {'template_name':'resturant/sign_in.html'}, name='resturant-sign-in'),
    url(r'^resturant/sign-out', auth_views.logout, 
    {'next_page':'/'}, name='resturant-sign-out'),
    url(r'^resturant/$', views.resturant_home, name='resturant-home'),
    url(r'^resturant/sign-up', views.resturant_sign_up, name='resturant-sign-up'),
    
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
