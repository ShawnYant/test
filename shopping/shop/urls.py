from . import views
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static

app_name = "shop"
namespace = 'shop'
urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.denglu,name='login'),
    path('register/',views.register,name='register'),
    path('shopping/',views.shouji,name='shopping'),
    path('shopping/<leibie_id>/',views.specific,name='specific'),
    path('shopping/<leibie_id>/<a_id>/',views.details,name='details'),
    # url('^(?P<category_slug>[-\w]+)/&', views.product_list, name='product_list_by_category'),
    # url('^((?P<id>\d+)/(?P<slug>[-\w]+)/)&', views.product_detail, name='product_detail'),
    # path('xiaomi/',views.xiaomi,name='xiaomi'),
]