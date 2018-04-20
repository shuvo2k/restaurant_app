
from django.conf.urls import url, include
from django.contrib import admin
from foodtaskerapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #resturant
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^resturant/sign-in/$', auth_views.login,
    {'template_name':'resturant/sign_in.html'}, name='resturant-sign-in'),
    url(r'^resturant/sign-out', auth_views.logout, 
    {'next_page':'/'}, name='resturant-sign-out'),
    url(r'^resturant/$', views.resturant_home, name='resturant-home'),
    url(r'^resturant/sign-up', views.resturant_sign_up, name='resturant-sign-up'),
    
    url(r'resturant/account/$', views.resturant_account, name='resturant-account'),
    url(r'resturant/meal/$', views.resturant_meal, name='resturant-meal'),
    url(r'resturant/meal/add/$', views.resturant_add_meal, name='resturant-add-meal'),
    url(r'resturant/meal/edit/(?P<meal_id>\d+)/$', views.resturant_edit_meal, name='resturant-edit-meal'),
    url(r'resturant/order/$', views.resturant_order, name='resturant-order'),
    url(r'resturant/report/$', views.resturant_report, name='resturant-report'),

    #sign in / sign up / sign out
    #(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    #/convert-token (sign in / sign up)
    #/remove-token (sign out)
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
