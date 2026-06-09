from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('officer/register/', views.officer_register, name='officer_register'),
    path('officer/login/', views.officer_login, name='officer_login'),
    path('post_complaint/', views.post_complaint, name='post_complaint'),
    path('complaint_list/', views.complaint_list, name='complaint_list'),
    path('feedback/<int:complaint_id>/', views.feedback, name='feedback'),
    path('admin/login/', views.admin_login, name='admin_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)