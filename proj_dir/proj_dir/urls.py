from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from backend.views import upload_document, download_word, download_pdf, report, history, register, delete_account, download_txt, clear_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/upload/'), name='home'),

    # URL-ы для аутентификации
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),  # Новый маршрут для регистрации
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('delete-account/', delete_account, name='delete_account'),

    # Ваши существующие URL-ы
    path('upload/', upload_document, name='upload'),
    path('report/<int:analysis_id>/', report, name='report'),
    path('history/', history, name='history'),
    path('clear-history/', clear_history, name='clear_history'),
    path('download/pdf/<int:analysis_id>/', download_pdf, name='download_pdf'),
    path('download/word/<int:analysis_id>/', download_word, name='download_word'),
    path('download/txt/<int:analysis_id>/', download_txt, name='download_txt'),
]

# Добавляем обработку статики и медиа в режиме разработки
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)