from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from loanApp import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/', include('loginApp.urls')),
    path('loan/', include('loanApp.urls')),
    path('manager/', include('managerApp.urls')),
    
   
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'loanApp.views.error_404_view'
